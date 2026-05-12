import hashlib
import json
import os
from pathlib import Path
import re
from typing import Dict, Iterable, List

import faiss
import numpy as np
import requests

from app.config import get_rag_settings, get_siliconflow_settings


class FAISSKnowledgeBase:
    """FAISS-based knowledge base for semantic search.
    Lightweight, no external service required, stores vectors as local files.
    """

    def __init__(self, model_name: str | None = None, collection_name: str | None = None):
        rag_settings = get_rag_settings()

        default_embedding_model = os.getenv("SILICONFLOW_EMBEDDING_MODEL", "Qwen/Qwen3-VL-Embedding-8B")
        self.model_name = model_name or default_embedding_model.strip() or "Qwen/Qwen3-VL-Embedding-8B"
        self.collection_name = collection_name or rag_settings.collection
        self.kb_dir = Path(rag_settings.kb_dir)
        self.kb_dir.mkdir(parents=True, exist_ok=True)

        # Path to FAISS index and metadata
        self.index_path = self.kb_dir / f"{self.collection_name}.faiss"
        self.metadata_path = self.kb_dir / f"{self.collection_name}_metadata.jsonl"
        self.manifest_path = self.kb_dir / f"{self.collection_name}_manifest.json"

        # Load or create index
        self._load_index()

    def _load_index(self) -> None:
        """Load existing FAISS index or create a new one."""
        if self.index_path.exists():
            self.index = faiss.read_index(str(self.index_path))
            self.embedding_dim = self.index.d
            # Load metadata
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
            return

        if self.index.d != embedding_dim:
            raise ValueError(
                f"Embedding dimension changed from {self.index.d} to {embedding_dim}; rebuild the index."
            )

    def _save_index(self) -> None:
        """Save FAISS index and metadata to disk."""
        if self.index is None:
            return

        faiss.write_index(self.index, str(self.index_path))
        with open(self.metadata_path, "w", encoding="utf-8") as f:
            for meta in self.metadata:
                f.write(json.dumps(meta, ensure_ascii=False) + "\n")

    def reset(self) -> None:
        """Remove the current FAISS index and metadata from memory and disk."""
        self.index = None
        self.embedding_dim = 0
        self.metadata = []
        for path in (self.index_path, self.metadata_path, self.manifest_path):
            if path.exists():
                path.unlink()

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

    @staticmethod
    def _window_text(text: str, chunk_size: int, overlap: int) -> List[str]:
        chunks: List[str] = []
        start = 0
        text = text.strip()
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            if end >= len(text):
                break
            start = max(0, end - overlap)
        return chunks

    def _split_markdown(self, text: str, chunk_size: int = 900, overlap: int = 120) -> List[str]:
        """Split markdown into heading-aware overlapping chunks."""
        normalized = text.replace("\r\n", "\n").replace("\r", "\n")
        lines = normalized.split("\n")
        sections: List[str] = []
        current: List[str] = []

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#") and current:
                section = "\n".join(current).strip()
                if section:
                    sections.append(section)
                current = [line]
                continue
            current.append(line)

        if current:
            section = "\n".join(current).strip()
            if section:
                sections.append(section)

        chunks: List[str] = []
        for section in sections:
            if len(section) <= chunk_size:
                chunks.append(section)
                continue
            chunks.extend(self._window_text(section, chunk_size, overlap))

        return chunks

    @staticmethod
    def _iter_markdown_files(library_dir: Path, recursive: bool = True) -> Iterable[Path]:
        pattern = "**/*.md" if recursive else "*.md"
        return sorted(path for path in library_dir.glob(pattern) if path.is_file())

    def index_document(
        self,
        text: str,
        source: str,
        chunk_size: int = 900,
        overlap: int = 120,
        path: str = "",
        save: bool = True,
    ) -> int:
        """Index a single document."""
        chunks = self._split_markdown(text, chunk_size, overlap)
        digest = hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()

        for chunk_idx, chunk in enumerate(chunks):
            embedding = self._embed(chunk)
            self._ensure_index(len(embedding))
            self.index.add(np.array([embedding]))
            # Store metadata
            self.metadata.append({
                "source": source,
                "path": path or source,
                "chunk_index": chunk_idx,
                "text": chunk[:200],
                "content": chunk,
                "content_sha256": digest,
            })

        if save:
            self._save_index()

        return len(chunks)

    def index_library(
        self,
        library_dir: str | None = None,
        chunk_size: int | None = None,
        overlap: int | None = None,
        reset: bool = True,
        recursive: bool = True,
    ) -> Dict:
        """Index all markdown files from a directory."""
        rag_settings = get_rag_settings()
        target_dir = library_dir or rag_settings.library_dir
        target_chunk_size = chunk_size or rag_settings.chunk_size
        target_overlap = overlap if overlap is not None else rag_settings.chunk_overlap

        lib_path = Path(target_dir)
        if not lib_path.exists():
            return {"status": "error", "message": f"Library directory {target_dir} not found"}

        if reset:
            self.reset()

        markdown_files = list(self._iter_markdown_files(lib_path, recursive=recursive))
        total_chunks = 0
        indexed_files = []

        for md_file in markdown_files:
            with open(md_file, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            rel_path = str(md_file.relative_to(lib_path)).replace("\\", "/")
            chunk_count = self.index_document(
                text,
                source=rel_path,
                chunk_size=target_chunk_size,
                overlap=target_overlap,
                path=str(md_file),
                save=False,
            )
            total_chunks += chunk_count
            indexed_files.append({"source": rel_path, "chunks": chunk_count})

        self._save_index()
        self._save_manifest(
            library_dir=str(lib_path),
            chunk_size=target_chunk_size,
            overlap=target_overlap,
            recursive=recursive,
            files=indexed_files,
        )

        return {
            "status": "ok",
            "files_indexed": len(markdown_files),
            "total_chunks": total_chunks,
            "collection": self.collection_name,
            "library_dir": str(lib_path),
            "chunk_size": target_chunk_size,
            "chunk_overlap": target_overlap,
        }

    def _save_manifest(
        self,
        library_dir: str,
        chunk_size: int,
        overlap: int,
        recursive: bool,
        files: List[Dict],
    ) -> None:
        manifest = {
            "collection": self.collection_name,
            "embedding_model": self.model_name,
            "library_dir": library_dir,
            "chunk_size": chunk_size,
            "chunk_overlap": overlap,
            "recursive": recursive,
            "files_indexed": len(files),
            "total_chunks": len(self.metadata),
            "files": files,
        }
        with open(self.manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)

    def status(self) -> Dict:
        manifest = {}
        if self.manifest_path.exists():
            with open(self.manifest_path, "r", encoding="utf-8") as f:
                manifest = json.load(f)

        index_total = int(self.index.ntotal) if self.index is not None else 0
        return {
            "collection": self.collection_name,
            "index_path": str(self.index_path),
            "metadata_path": str(self.metadata_path),
            "indexed": self.index is not None and index_total > 0,
            "vectors": index_total,
            "metadata_rows": len(self.metadata),
            "embedding_dim": self.embedding_dim,
            "manifest": manifest,
        }

    def query(self, question: str, top_k: int | None = None) -> List[Dict]:
        """Query the knowledge base and return top-k results."""
        if self.index is None or self.index.ntotal == 0:
            return []

        rag_settings = get_rag_settings()
        result_count = top_k or rag_settings.top_k
        query_embedding = self._embed(question)

        candidate_k = max(result_count * 8, result_count)
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
        filtered = [c for c in candidates if c.get("score", 0.0) >= rag_settings.min_score]
        if not filtered:
            filtered = sorted(candidates, key=lambda x: x.get("score", 0.0), reverse=True)[: max(result_count, 1)]

        # Diversify near-duplicate chunks while preserving relevance.
        results = self._mmr_select(filtered, top_k=result_count)
        if not results:
            results = sorted(filtered, key=lambda x: x.get("score", 0.0), reverse=True)[:result_count]

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
