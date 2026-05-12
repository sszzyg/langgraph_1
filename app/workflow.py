from functools import lru_cache
from typing import AsyncGenerator, Literal, TypedDict

from langgraph.graph import END, START, StateGraph

from app.case_engine import build_case_checklist_report, render_case_report_text
from app.config import get_rag_settings
from app.faiss_kb import FAISSKnowledgeBase, render_kb_answer
from app.kimi_client import KimiClient
from app.local_chatbot import LocalChatbot


class WorkflowState(TypedDict, total=False):
    input: str
    strategy: str
    route: str
    answer: str
    conversation_id: str
    case_id: str
    checklist_coverage: float


def run_workflow(user_input: str, conversation_id: str = "", strategy: str = "") -> WorkflowState:
    graph = build_graph()
    return graph.invoke(
        {
            "input": user_input,
            "conversation_id": conversation_id,
            "strategy": strategy,
        }
    )


async def stream_workflow_events(
    user_input: str, conversation_id: str = "", strategy: str = ""
) -> AsyncGenerator[dict, None]:
    """异步生成器：逐步产生工作流进度事件，最后 yield 含 type='answer' 的最终结果。"""

    yield {"step": "routing", "message": "正在分析问题类型…"}

    text = user_input.strip().lower()
    strat = strategy.strip().lower()

    if not text:
        yield {
            "type": "answer",
            "answer": "请输入问题后再试。",
            "conversation_id": conversation_id,
            "route": "empty",
            "case_id": "",
            "checklist_coverage": 0.0,
        }
        return

    # ---- 路由判断 ----
    if strat == "checklist":
        route = "checklist"
    elif strat in {"kb", "chroma", "local"}:
        route = "kb"
    elif strat in {"llm", "rag"}:
        route = "llm"
    elif any(t in text for t in ["ccr", "car-to-car", "案例", "参数", "checklist", "清单"]):
        route = "checklist"
    elif any(t in text for t in ["help", "帮助", "怎么", "如何"]):
        route = "guide"
    else:
        route = "llm"

    yield {"step": "routed", "message": f"已确定处理策略：{route}"}

    # ---- guide ----
    if route == "guide":
        yield {
            "type": "answer",
            "answer": (
                "这是一个 LangGraph + 本地知识库工作流示例。\n"
                "你可以直接提问，或在请求中设置 strategy=kb 走知识库检索，"
                "strategy=llm 走知识库+AI大模型回答，strategy=checklist 生成测试清单。"
            ),
            "conversation_id": conversation_id,
            "route": route,
            "case_id": "",
            "checklist_coverage": 0.0,
        }
        return

    # ---- checklist ----
    if route == "checklist":
        yield {"step": "checklist", "message": "正在生成测试清单…"}
        report = build_case_checklist_report(user_input)
        yield {
            "type": "answer",
            "answer": render_case_report_text(report),
            "conversation_id": conversation_id,
            "route": route,
            "case_id": report.get("case_id", ""),
            "checklist_coverage": float(report.get("coverage", 0.0)),
        }
        return

    # ---- 知识库检索（kb / llm 均需要）----
    yield {"step": "kb_search", "message": "正在检索知识库，查找相关片段…"}
    rag_settings = get_rag_settings()
    kb = FAISSKnowledgeBase()
    hits = kb.query(user_input, top_k=rag_settings.top_k)
    yield {
        "step": "kb_done",
        "message": f"知识库检索完成，共找到 {len(hits)} 个相关片段",
    }

    # ---- kb 策略：直接返回检索结果 ----
    if route == "kb":
        yield {
            "type": "answer",
            "answer": render_kb_answer(user_input, hits),
            "conversation_id": conversation_id,
            "route": route,
            "case_id": "",
            "checklist_coverage": 0.0,
        }
        return

    # ---- llm 策略：将检索片段送入大模型 ----
    if not hits:
        yield {
            "type": "answer",
            "answer": "知识库中暂未检索到相关片段。请先确认 Markdown 文档已入库，或换一种问法再试。",
            "conversation_id": conversation_id,
            "route": route,
            "case_id": "",
            "checklist_coverage": 0.0,
        }
        return

    context = _format_kb_context(hits)
    yield {"step": "llm_call", "message": "正在调用 AI 大模型生成综合回答…"}

    try:
        client = KimiClient()
        answer = _append_sources(client.chat(user_input, context=context), hits)
        yield {
            "type": "answer",
            "answer": answer,
            "conversation_id": conversation_id,
            "route": route,
            "case_id": "",
            "checklist_coverage": 0.0,
        }
    except Exception:  # noqa: BLE001
        yield {"step": "llm_fallback", "message": "AI 模型不可用，切换到本地知识库回答…"}
        fallback = LocalChatbot(top_k=rag_settings.top_k).chat(query=user_input, conversation_id=conversation_id)
        fb_answer = fallback.get("answer", "")
        if fb_answer:
            fb_answer = "（AI 模型未配置或暂不可用，以下为本地知识库检索结果）\n\n" + fb_answer
        yield {
            "type": "answer",
            "answer": fb_answer,
            "conversation_id": fallback.get("conversation_id", conversation_id),
            "route": route,
            "case_id": "",
            "checklist_coverage": 0.0,
        }



def route_intent(state: WorkflowState) -> WorkflowState:
    text = state.get("input", "").strip().lower()
    strategy = state.get("strategy", "").strip().lower()
    if not text:
        return {"route": "empty", "answer": "请输入问题后再试。"}

    if strategy == "checklist":
        return {"route": "checklist"}

    if strategy in {"kb", "chroma", "local"}:
        return {"route": "kb"}

    if strategy in {"llm", "rag"}:
        return {"route": "llm"}

    if any(token in text for token in ["help", "帮助", "怎么", "如何"]):
        return {"route": "guide"}

    if any(token in text for token in ["ccr", "car-to-car", "案例", "参数", "checklist", "清单"]):
        return {"route": "checklist"}

    if any(token in text for token in ["ncap", "protocol", "文档", "知识库", "标准"]):
        return {"route": "llm"}

    return {"route": "llm"}



def _format_kb_context(hits: list[dict]) -> str:
    if not hits:
        return ""

    parts = []
    for idx, hit in enumerate(hits, start=1):
        meta = hit.get("metadata", {}) or {}
        source = meta.get("source") or hit.get("source") or "unknown"
        chunk_index = meta.get("chunk_index", hit.get("chunk_index", 0))
        score = hit.get("rerank_score", hit.get("score", 0.0))
        text = hit.get("text", "")
        parts.append(f"[{idx}] source: {source}#{chunk_index} | score: {float(score):.4f}\n{text}")

    return "\n\n".join(parts)


def _append_sources(answer: str, hits: list[dict]) -> str:
    if not hits:
        return answer

    lines = ["\n\n来源:"]
    for idx, hit in enumerate(hits, start=1):
        meta = hit.get("metadata", {}) or {}
        source = meta.get("source") or hit.get("source") or "unknown"
        chunk_index = meta.get("chunk_index", hit.get("chunk_index", 0))
        score = hit.get("rerank_score", hit.get("score", 0.0))
        lines.append(f"[{idx}] {source}#{chunk_index} (score={float(score):.4f})")

    return answer.rstrip() + "\n".join(lines)


def call_llm(state: WorkflowState) -> WorkflowState:
    question = state.get("input", "")
    conversation_id = state.get("conversation_id", "")

    rag_settings = get_rag_settings()
    kb = FAISSKnowledgeBase()
    hits = kb.query(question, top_k=rag_settings.top_k)
    if not hits:
        return {
            "answer": "知识库中暂未检索到相关片段。请先确认 Markdown 文档已入库，或换一种问法再试。",
            "conversation_id": conversation_id,
        }

    context = _format_kb_context(hits)

    try:
        client = KimiClient()
        answer = _append_sources(client.chat(question, context=context), hits)
        return {
            "answer": answer,
            "conversation_id": conversation_id,
        }
    except Exception:  # noqa: BLE001
        fallback = LocalChatbot(top_k=rag_settings.top_k).chat(query=question, conversation_id=conversation_id)
        answer = fallback.get("answer", "")
        if answer:
            answer = "（Kimi 未配置或暂不可用，已使用本地知识库回答）\n\n" + answer
        return {
            "answer": answer,
            "conversation_id": fallback.get("conversation_id", conversation_id),
        }



def guide_response(_: WorkflowState) -> WorkflowState:
    return {
        "answer": (
            "这是一个 LangGraph + Markdown RAG 知识库工作流示例。"
            "将 Markdown 放入 app/library 后，调用 /v1/knowledge/index 重建索引；"
            "提问时设置 strategy=llm 走知识库检索 + 大模型综合回答，"
            "或设置 strategy=kb 直接返回检索片段。"
        )
    }



def run_case_checklist(state: WorkflowState) -> WorkflowState:
    report = build_case_checklist_report(state.get("input", ""))
    return {
        "answer": render_case_report_text(report),
        "case_id": report.get("case_id", ""),
        "checklist_coverage": float(report.get("coverage", 0.0)),
    }



def run_kb_retrieval(state: WorkflowState) -> WorkflowState:
    rag_settings = get_rag_settings()
    kb = FAISSKnowledgeBase()
    question = state.get("input", "")
    hits = kb.query(question, top_k=rag_settings.top_k)
    return {"answer": render_kb_answer(question, hits)}



def pick_next_node(state: WorkflowState) -> Literal["guide", "llm", "checklist", "kb", "end"]:
    route = state.get("route", "llm")
    if route == "empty":
        return "end"
    if route == "guide":
        return "guide"
    if route == "checklist":
        return "checklist"
    if route == "kb":
        return "kb"
    return "llm"



@lru_cache(maxsize=1)
def build_graph():
    graph_builder = StateGraph(WorkflowState)

    graph_builder.add_node("router", route_intent)
    graph_builder.add_node("guide", guide_response)
    graph_builder.add_node("llm", call_llm)
    graph_builder.add_node("checklist", run_case_checklist)
    graph_builder.add_node("kb", run_kb_retrieval)

    graph_builder.add_edge(START, "router")
    graph_builder.add_conditional_edges(
        "router",
        pick_next_node,
        {
            "guide": "guide",
            "llm": "llm",
            "checklist": "checklist",
            "kb": "kb",
            "end": END,
        },
    )
    graph_builder.add_edge("guide", END)
    graph_builder.add_edge("llm", END)
    graph_builder.add_edge("checklist", END)
    graph_builder.add_edge("kb", END)

    return graph_builder.compile()
