from typing import Dict, List

from app.faiss_kb import FAISSKnowledgeBase


class LocalChatbot:
    """A very small local chatbot that uses FAISS KB for retrieval
    and returns a synthesized answer by concatenating top-k hits.
    This is intentionally lightweight and does not call any external LLM.
    """

    def __init__(self, top_k: int = 4):
        self.kb = FAISSKnowledgeBase()
        self.top_k = top_k

    def chat(self, query: str, conversation_id: str = "") -> Dict[str, str]:
        hits = self.kb.query(query, top_k=self.top_k)
        if not hits:
            return {"answer": "抱歉，知识库中未找到相关内容。", "conversation_id": conversation_id}

        parts: List[str] = []
        for idx, hit in enumerate(hits, start=1):
            meta = hit.get("metadata", {}) or {}
            src = meta.get("source") or meta.get("filename") or "unknown"
            text = hit.get("text") or hit.get("content") or ""
            parts.append(f"[{idx}] 来源: {src}\n{text}")

        assembled = "\n\n".join(parts)
        answer = (
            "根据知识库检索到以下相关片段：\n\n"
            + assembled
            + "\n\n以上为检索结果。你可以据此提问或要求更精确的节选。"
        )

        return {"answer": answer, "conversation_id": conversation_id}
