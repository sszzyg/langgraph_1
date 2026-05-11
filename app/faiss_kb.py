import os
from pathlib import Path
from typing import List, Dict
import re

import faiss
import numpy as np
import requests

from app.config import get_siliconflow_settings


class FAISSKnowledgeBase:
    """FAISS-based knowledge base for semantic search.
    Lightweight, no external service required, stores vectors as local files.
    """

    def __init__(self, model_name: str = "Qwen/Qwen3-VL-Embedding-8B", collection_name: str = "ncap_library"):
        self.model_name = model_name
        self.collection_name = collection_name
        self.kb_dir = Path(os.getenv("KB_DIR", ".faiss"))
        self.kb_dir.mkdir(exist_ok=True)

        # Path to FAISS index and metadata
        self.index_path = self.kb_dir / f"{collection_name}.faiss"
        self.metadata_path = self.kb_dir / f"{collection_name}_metadata.jsonl"

        # Load or create index
        self._load_index()

    def _load_index(self) -> None:
        """Load existing FAISS index or create a new one."""
        if self.index_path.exists():
            self.index = faiss.read_index(str(self.index_path))
            self.embedding_dim = self.index.d
            # Load metadata
            import json
            self.metadata = []
            if self.metadata_path.exists():
                with open(self.metadata_path, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            self.metadata.append(json.loads(line))
        else:
            # Create new index after we know embedding dimension
            self.index = None
            self.embedding_dim = 0
            self.metadata = []

    def _ensure_index(self, embedding_dim: int) -> None:
        if self.index is None:
            self.embedding_dim = embedding_dim
            # Flat L2 index is lightweight and CPU-friendly
            self.index = faiss.IndexFlatL2(self.embedding_dim)

    def _save_index(self) -> None:
        """Save FAISS index and metadata to disk."""
        if self.index is None:
            return

        faiss.write_index(self.index, str(self.index_path))
        import json
        with open(self.metadata_path, "w", encoding="utf-8") as f:
            for meta in self.metadata:
                f.write(json.dumps(meta, ensure_ascii=False) + "\n")

    def _embed(self, text: str) -> np.ndarray:
        settings = get_siliconflow_settings()
        url = f"{settings.base_url}/embeddings"
        headers = {
            "Authorization": f"Bearer {settings.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "input": text,
            "model": settings.embedding_model,
        }

        response = requests.post(url, json=payload, headers=headers, timeout=settings.timeout_seconds)
        response.raise_for_status()
        data = response.json()

        embedding = (data.get("data") or [{}])[0].get("embedding")
        if not embedding:
            raise ValueError("Empty embedding from SiliconFlow.")

        vector = np.array(embedding, dtype="float32")
        return self._l2_normalize(vector)

    @staticmethod
    def _l2_normalize(vector: np.ndarray) -> np.ndarray:
        norm = np.linalg.norm(vector)
        if norm == 0.0:
            return vector
        return vector / norm

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        # Keep both English words and CJK characters to support mixed-language queries.
        tokens = re.findall(r"[a-zA-Z0-9_]+|[\u4e00-\u9fff]", text.lower())
        return [t for t in tokens if t.strip()]

    def _lexical_score(self, query: str, doc: str) -> float:
        q_tokens = self._tokenize(query)
        d_tokens = self._tokenize(doc)
        if not q_tokens or not d_tokens:
            return 0.0

        q_set = set(q_tokens)
        d_set = set(d_tokens)
        overlap = q_set & d_set
        if not overlap:
            return 0.0

        recall_like = len(overlap) / max(1, len(q_set))
        precision_like = len(overlap) / max(1, len(d_set))
        # Slightly favor query-term coverage while keeping precision signal.
        return float(0.7 * recall_like + 0.3 * precision_like)

    @staticmethod
    def _semantic_score_from_distance(distance: float) -> float:
        # For normalized vectors: L2^2 = 2 - 2*cos, so similarity ~= 1 - d/2.
        score = 1.0 - (float(distance) / 2.0)
        if score < 0.0:
            return 0.0
        if score > 1.0:
            return 1.0
        return score

    def _mmr_select(
        self,
        candidates: List[Dict],
        top_k: int,
        lambda_weight: float = 0.75,
    ) -> List[Dict]:
        if not candidates:
            return []

        selected: List[Dict] = []
        remaining = candidates.copy()

        while remaining and len(selected) < top_k:
            best_idx = 0
            best_score = -1e9

            for idx, cand in enumerate(remaining):
                relevance = float(cand.get("score", 0.0))
                penalty = 0.0

                cand_emb = cand.get("embedding")
                if selected and isinstance(cand_emb, np.ndarray):
                    max_similarity_to_selected = 0.0
                    for picked in selected:
                        picked_emb = picked.get("embedding")
                        if not isinstance(picked_emb, np.ndarray):
                            continue
                        sim = float(np.dot(cand_emb, picked_emb))
                        if sim > max_similarity_to_selected:
                            max_similarity_to_selected = sim
                    penalty = max_similarity_to_selected

                mmr_score = lambda_weight * relevance - (1.0 - lambda_weight) * penalty
                if mmr_score > best_score:
                    best_score = mmr_score
                    best_idx = idx

            selected.append(remaining.pop(best_idx))

        return selected

    def _split_markdown(self, text: str, chunk_size: int = 500, overlap: int = 80) -> List[str]:
        """Split markdown text into overlapping chunks."""
        chunks = []
        lines = text.split("\n")
        current_chunk = []
        current_size = 0

        for line in lines:
            current_chunk.append(line)
            current_size += len(line) + 1  # +1 for newline
            if current_size >= chunk_size:
                chunk_text = "\n".join(current_chunk).strip()
                if chunk_text:
                    chunks.append(chunk_text)
                # Keep last lines for overlap
                overlap_lines = int(overlap / 30) if overlap > 0 else 0
                current_chunk = current_chunk[-overlap_lines:] if overlap_lines > 0 else []
                current_size = sum(len(line) + 1 for line in current_chunk)

        if current_chunk:
            chunk_text = "\n".join(current_chunk).strip()
            if chunk_text:
                chunks.append(chunk_text)

        return chunks

    def index_document(self, text: str, source: str, chunk_size: int = 500, overlap: int = 80) -> None:
        """Index a single document."""
        chunks = self._split_markdown(text, chunk_size, overlap)

        for chunk_idx, chunk in enumerate(chunks):
            embedding = self._embed(chunk)
            self._ensure_index(len(embedding))
            self.index.add(np.array([embedding]))
            # Store metadata
            self.metadata.append({
                "source": source,
                "chunk_index": chunk_idx,
                "text": chunk[:200],
                "content": chunk,
            })

        self._save_index()

    def index_library(self, library_dir: str = "app/library", chunk_size: int = 500, overlap: int = 80) -> Dict:
        """Index all markdown files from a directory."""
        lib_path = Path(library_dir)
        if not lib_path.exists():
            return {"status": "error", "message": f"Library directory {library_dir} not found"}

        markdown_files = list(lib_path.glob("*.md"))
        total_chunks = 0

        for md_file in markdown_files:
            with open(md_file, "r", encoding="utf-8") as f:
                text = f.read()
            chunks = self._split_markdown(text, chunk_size, overlap)
            self.index_document(text, md_file.name, chunk_size, overlap)
            total_chunks += len(chunks)

        return {
            "status": "ok",
            "files_indexed": len(markdown_files),
            "total_chunks": total_chunks,
            "collection": self.collection_name,
        }

    def query(self, question: str, top_k: int = 4) -> List[Dict]:
        """Query the knowledge base and return top-k results."""
        if self.index is None or self.index.ntotal == 0:
            return []

        query_embedding = self._embed(question)

        candidate_k = max(top_k * 8, top_k)
        candidate_k = min(candidate_k, int(self.index.ntotal))

        # Search a larger candidate pool first, then rerank.
        distances, indices = self.index.search(np.array([query_embedding]), candidate_k)

        candidates = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx < len(self.metadata) and idx >= 0:
                meta = self.metadata[idx]
                text = meta.get("content") or meta.get("text", "")
                lexical_score = self._lexical_score(question, text)
                semantic_score = self._semantic_score_from_distance(float(distance))
                score = 0.8 * semantic_score + 0.2 * lexical_score

                candidate = {
                    "text": text,
                    "source": meta.get("source", ""),
                    "chunk_index": meta.get("chunk_index", 0),
                    "distance": float(distance),
                    "semantic_score": semantic_score,
                    "lexical_score": lexical_score,
                    "score": score,
                    "metadata": meta,
                }

                # Try attaching embedding for MMR diversity selection.
                try:
                    candidate["embedding"] = self.index.reconstruct(int(idx))
                except Exception:
                    candidate["embedding"] = None

                candidates.append(candidate)

        if not candidates:
            return []

        # Keep all obviously relevant candidates, otherwise fallback to top by score.
        filtered = [c for c in candidates if c.get("score", 0.0) >= 0.38]
        if not filtered:
            filtered = sorted(candidates, key=lambda x: x.get("score", 0.0), reverse=True)[: max(top_k, 1)]

        # Diversify near-duplicate chunks while preserving relevance.
        results = self._mmr_select(filtered, top_k=top_k)
        if not results:
            results = sorted(filtered, key=lambda x: x.get("score", 0.0), reverse=True)[:top_k]

        # Cleanup non-serializable runtime field.
        for hit in results:
            hit.pop("embedding", None)

        settings = get_siliconflow_settings()
        if settings.rerank_enabled and results:
            results = self._rerank(question, results, settings)

        return results

    def _rerank(self, query: str, results: List[Dict], settings) -> List[Dict]:
        url = f"{settings.base_url}/rerank"
        headers = {
            "Authorization": f"Bearer {settings.api_key}",
            "Content-Type": "application/json",
        }
        documents = [hit.get("text", "") for hit in results]
        payload = {
            "model": settings.rerank_model,
            "query": query,
            "documents": documents,
            "return_documents": True,
            "top_n": len(documents),
        }

        response = requests.post(url, json=payload, headers=headers, timeout=settings.timeout_seconds)
        response.raise_for_status()
        data = response.json()

        rerank_results = data.get("results") or []
        if not rerank_results:
            return results

        reranked = []
        for item in rerank_results:
            index = item.get("index")
            if index is None or index >= len(results):
                continue
            hit = results[index]
            hit["rerank_score"] = float(item.get("relevance_score", 0.0))
            reranked.append(hit)

        return reranked or results


def render_kb_answer(question: str, hits: List[Dict]) -> str:
    """Format knowledge base query results into a readable answer."""
    if not hits:
        return "抱歉，知识库中未找到相关内容。"

    parts = []
    for idx, hit in enumerate(hits, start=1):
        source = hit.get("source", "unknown")
        text = hit.get("text", "")
        parts.append(f"[{idx}] 来源: {source}\n{text}")

    assembled = "\n\n".join(parts)
    return (
        "根据知识库检索到以下相关片段：\n\n"
        + assembled
        + "\n\n以上为检索结果。你可以据此提问或要求更精确的节选。"
    )
