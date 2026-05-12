import json
import os
from pathlib import Path

from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from pydantic import BaseModel, Field

from app.config import get_rag_settings
from app.faiss_kb import FAISSKnowledgeBase
from app.workflow import run_workflow, stream_workflow_events


app = FastAPI(
    title="LangGraph Tool API",
    version="1.3.0",
    description=(
        "OpenAPI-compatible HTTP tool for LangGraph Markdown RAG. "
        "Use POST /v1/tools/langgraph/run as the primary operation."
    ),
)

STATIC_DIR = Path(__file__).resolve().parent / "static"
INDEX_FILE = STATIC_DIR / "index.html"

def verify_tool_api_key(
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
) -> None:
    # Optional hardening for public deployment.
    required_key = os.getenv("TOOL_API_KEY", "").strip()
    if required_key and x_api_key != required_key:
        raise HTTPException(status_code=401, detail="Unauthorized")


class ToolRequest(BaseModel):
    query: str = Field(..., description="User question or task to send into the LangGraph workflow.")
    conversation_id: str = Field(default="", description="Optional conversation id for multi-turn sessions.")
    strategy: str = Field(
        default="default",
        description="Execution strategy: default, checklist, kb/local, or llm/rag (KB + LLM).",
    )


class ToolResponse(BaseModel):
    answer: str
    conversation_id: str = ""
    route: str = ""
    case_id: str = ""
    checklist_coverage: float = 0.0


class ErrorResponse(BaseModel):
    error: str = Field(..., description="Error summary.")
    detail: str = Field(..., description="Readable detail for troubleshooting.")


class KnowledgeIndexRequest(BaseModel):
    library_dir: str | None = Field(
        default=None,
        description="Directory containing markdown files. Defaults to KB_LIBRARY_DIR.",
    )
    chunk_size: int | None = Field(
        default=None,
        ge=200,
        description="Maximum characters per chunk. Defaults to KB_CHUNK_SIZE.",
    )
    chunk_overlap: int | None = Field(
        default=None,
        ge=0,
        description="Overlapping characters between chunks. Defaults to KB_CHUNK_OVERLAP.",
    )
    reset: bool = Field(
        default=True,
        description="Whether to rebuild the FAISS index before ingesting markdown files.",
    )
    recursive: bool = Field(
        default=True,
        description="Whether to scan markdown files recursively under library_dir.",
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(_: Request, exc: HTTPException) -> JSONResponse:
    labels = {
        400: "BadRequest",
        401: "Unauthorized",
        500: "InternalError",
    }
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": labels.get(exc.status_code, "HttpError"),
            "detail": str(exc.detail),
        },
    )


@app.get("/health")
def health_check() -> dict[str, str | bool | int]:
    kb_status = FAISSKnowledgeBase().status()
    return {
        "status": "ok",
        "kb_indexed": bool(kb_status.get("indexed", False)),
        "kb_vectors": int(kb_status.get("vectors", 0)),
    }


@app.get("/", include_in_schema=False)
def frontend() -> FileResponse:
    return FileResponse(INDEX_FILE)


@app.get(
    "/v1/knowledge/status",
    tags=["knowledge"],
    summary="Get markdown knowledge-base index status",
)
def knowledge_status(_: None = Depends(verify_tool_api_key)) -> dict:
    return FAISSKnowledgeBase().status()


@app.post(
    "/v1/knowledge/index",
    tags=["knowledge"],
    summary="Rebuild markdown knowledge-base index",
)
def rebuild_knowledge_index(
    payload: KnowledgeIndexRequest | None = None,
    _: None = Depends(verify_tool_api_key),
) -> dict:
    settings = get_rag_settings()
    request = payload or KnowledgeIndexRequest()
    chunk_size = request.chunk_size or settings.chunk_size
    chunk_overlap = request.chunk_overlap if request.chunk_overlap is not None else settings.chunk_overlap
    if chunk_overlap >= chunk_size:
        raise HTTPException(status_code=400, detail="chunk_overlap must be smaller than chunk_size")

    try:
        result = FAISSKnowledgeBase().index_library(
            library_dir=request.library_dir or settings.library_dir,
            chunk_size=chunk_size,
            overlap=chunk_overlap,
            reset=request.reset,
            recursive=request.recursive,
        )
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    if result.get("status") == "error":
        raise HTTPException(status_code=400, detail=result.get("message", "indexing failed"))
    return result


@app.post(
    "/v1/tools/langgraph/run",
    response_model=ToolResponse,
    tags=["tools"],
    summary="Execute LangGraph workflow",
    operation_id="runLanggraphTool",
    responses={
        400: {
            "model": ErrorResponse,
            "description": "Invalid request.",
        },
        401: {
            "model": ErrorResponse,
            "description": "Unauthorized.",
        },
        500: {
            "model": ErrorResponse,
            "description": "Workflow execution failed.",
        },
    },
)
def run_langgraph_tool(
    payload: ToolRequest,
    _: None = Depends(verify_tool_api_key),
) -> ToolResponse:
    if not payload.query.strip():
        raise HTTPException(status_code=400, detail="query must not be empty")

    try:
        result = run_workflow(
            payload.query,
            payload.conversation_id or "",
            payload.strategy or "default",
        )
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return ToolResponse(
        answer=result.get("answer", ""),
        conversation_id=result.get("conversation_id", ""),
        route=result.get("route", ""),
        case_id=result.get("case_id", ""),
        checklist_coverage=float(result.get("checklist_coverage", 0.0)),
    )


@app.post(
    "/v1/tools/langgraph/stream",
    tags=["tools"],
    summary="Stream LangGraph workflow progress via SSE",
    operation_id="streamLanggraphTool",
)
async def stream_langgraph_tool(
    payload: ToolRequest,
    _: None = Depends(verify_tool_api_key),
) -> StreamingResponse:
    """流式端点：通过 Server-Sent Events 实时返回每个处理步骤和最终答案。"""
    if not payload.query.strip():
        raise HTTPException(status_code=400, detail="query must not be empty")

    async def event_generator():
        try:
            async for event in stream_workflow_events(
                payload.query,
                payload.conversation_id or "",
                payload.strategy or "default",
            ):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
        except Exception as exc:  # noqa: BLE001
            error_event = {"type": "error", "message": str(exc)}
            yield f"data: {json.dumps(error_event, ensure_ascii=False)}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@app.post(
    "/tool/langgraph/query",
    response_model=ToolResponse,
    tags=["tools"],
    summary="Legacy endpoint, use /v1/tools/langgraph/run",
    operation_id="runLanggraphToolLegacy",
    deprecated=True,
)
def langgraph_query_legacy(
    payload: ToolRequest,
    _: None = Depends(verify_tool_api_key),
) -> ToolResponse:
    return run_langgraph_tool(payload)
