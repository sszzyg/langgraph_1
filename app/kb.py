from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
from typing import Iterable, List

import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

from app.config import get_chroma_settings


ROOT_DIR = Path(__file__).resolve().parent.parent
LIBRARY_DIR = ROOT_DIR / "app" / "library"
LOCAL_CHROMA_DIR = ROOT_DIR / ".chroma"


@dataclass
class KbHit:
    source: str
    chunk_id: str
    distance: float
    content: str


class ChromaKnowledgeBase:
    def __init__(self) -> None:
        settings = get_chroma_settings()
        self.collection_name = settings.collection
        self.chunk_size = settings.chunk_size
        self.chunk_overlap = settings.chunk_overlap

        self.client = self._build_client(
            host=settings.host,
            port=settings.port,
            ssl=settings.ssl,
        )
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=DefaultEmbeddingFunction(),
            metadata={"hnsw:space": "cosine"},
        )

    def _build_client(self, host: str, port: int, ssl: bool):
        try:
            client = chromadb.HttpClient(host=host, port=port, ssl=ssl)
            client.heartbeat()
            return client
        except Exception:
            LOCAL_CHROMA_DIR.mkdir(parents=True, exist_ok=True)
            return chromadb.PersistentClient(path=str(LOCAL_CHROMA_DIR))

    def _split_markdown(self, text: str) -> List[str]:
        lines = text.splitlines()
        blocks: List[str] = []
        buf: List[str] = []

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#") and buf:
                blocks.append("\n".join(buf).strip())
                buf = [line]
                continue
            buf.append(line)

        if buf:
            blocks.append("\n".join(buf).strip())

        chunks: List[str] = []
        for block in blocks:
            start = 0
            while start < len(block):
                end = min(start + self.chunk_size, len(block))
                chunk = block[start:end].strip()
                if chunk:
                    chunks.append(chunk)
                if end >= len(block):
                    break
                start = max(0, end - self.chunk_overlap)
        return chunks

    def _iter_markdown_files(self, folder: Path) -> Iterable[Path]:
        if not folder.exists():
            return []
        return sorted(folder.glob("*.md"))

    def _upsert_file(self, file_path: Path) -> int:
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        chunks = self._split_markdown(text)
        if not chunks:
            return 0

        ids: List[str] = []
        docs: List[str] = []
        metas: List[dict] = []

        for idx, chunk in enumerate(chunks):
            digest = hashlib.md5(f"{file_path.name}:{idx}:{len(chunk)}".encode("utf-8")).hexdigest()
            chunk_id = f"{file_path.stem}-{idx}-{digest[:8]}"
            ids.append(chunk_id)
            docs.append(chunk)
            metas.append(
                {
                    "source": file_path.name,
                    "chunk_index": idx,
                    "path": str(file_path.relative_to(ROOT_DIR)).replace("\\", "/"),
                }
            )

        self.collection.upsert(ids=ids, documents=docs, metadatas=metas)
        return len(chunks)

    def index_library(self, folder: Path | None = None) -> dict:
        target = folder or LIBRARY_DIR
        files = list(self._iter_markdown_files(target))
        total_chunks = 0

        for file_path in files:
            total_chunks += self._upsert_file(file_path)

        return {
            "files": len(files),
            "chunks": total_chunks,
            "collection": self.collection_name,
            "folder": str(target),
        }

    def query(self, question: str, top_k: int = 4) -> List[KbHit]:
        result = self.collection.query(
            query_texts=[question],
            n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )

        docs = result.get("documents", [[]])[0]
        metas = result.get("metadatas", [[]])[0]
        distances = result.get("distances", [[]])[0]

        hits: List[KbHit] = []
        for doc, meta, distance in zip(docs, metas, distances):
            source = (meta or {}).get("source", "unknown.md")
            chunk_index = (meta or {}).get("chunk_index", -1)
            hits.append(
                KbHit(
                    source=source,
                    chunk_id=f"{source}#{chunk_index}",
                    distance=float(distance),
                    content=doc,
                )
            )

        return hits


def render_kb_answer(question: str, hits: List[KbHit]) -> str:
    if not hits:
        return "没有检索到知识库内容，请确认文档已入库。"

    lines = [
        f"问题: {question}",
        "以下是知识库检索结果（按相似度排序）:",
    ]

    for idx, hit in enumerate(hits, start=1):
        excerpt = " ".join(hit.content.split())
        if len(excerpt) > 260:
            excerpt = excerpt[:260] + "..."
        lines.append(f"{idx}. 来源: {hit.source} | 片段: {hit.chunk_id} | 距离: {hit.distance:.4f}")
        lines.append(f"   摘要: {excerpt}")

    return "\n".join(lines)
