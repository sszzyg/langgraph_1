from dataclasses import dataclass
import os

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class DifySettings:
    base_url: str
    api_key: str
    user: str
    timeout_seconds: int = 60


@dataclass(frozen=True)
class ChromaSettings:
    host: str
    port: int
    ssl: bool
    collection: str
    top_k: int
    chunk_size: int
    chunk_overlap: int


@dataclass(frozen=True)
class KimiSettings:
    base_url: str
    api_key: str
    model: str
    temperature: float
    top_p: float
    max_tokens: int
    timeout_seconds: int = 60


@dataclass(frozen=True)
class SiliconFlowSettings:
    base_url: str
    api_key: str
    embedding_model: str
    rerank_model: str
    rerank_enabled: bool
    timeout_seconds: int = 60


def get_settings() -> DifySettings:
    base_url = os.getenv("DIFY_BASE_URL", "").strip().rstrip("/")
    api_key = os.getenv("DIFY_API_KEY", "").strip()
    user = os.getenv("DIFY_USER", "langgraph-user").strip() or "langgraph-user"

    timeout_raw = os.getenv("DIFY_TIMEOUT_SECONDS", "60").strip()
    try:
        timeout_seconds = int(timeout_raw)
    except ValueError:
        timeout_seconds = 60

    if not base_url:
        raise ValueError("DIFY_BASE_URL is required.")
    if not api_key:
        raise ValueError("DIFY_API_KEY is required.")

    return DifySettings(
        base_url=base_url,
        api_key=api_key,
        user=user,
        timeout_seconds=timeout_seconds,
    )


def get_chroma_settings() -> ChromaSettings:
    host = os.getenv("CHROMA_HOST", "127.0.0.1").strip() or "127.0.0.1"

    port_raw = os.getenv("CHROMA_PORT", "8001").strip()
    try:
        port = int(port_raw)
    except ValueError:
        port = 8001

    ssl_raw = os.getenv("CHROMA_SSL", "false").strip().lower()
    ssl = ssl_raw in {"1", "true", "yes", "on"}

    collection = os.getenv("CHROMA_COLLECTION", "ncap_library").strip() or "ncap_library"

    top_k_raw = os.getenv("CHROMA_TOP_K", "4").strip()
    try:
        top_k = int(top_k_raw)
    except ValueError:
        top_k = 4

    chunk_size_raw = os.getenv("CHROMA_CHUNK_SIZE", "500").strip()
    try:
        chunk_size = int(chunk_size_raw)
    except ValueError:
        chunk_size = 500

    overlap_raw = os.getenv("CHROMA_CHUNK_OVERLAP", "80").strip()
    try:
        chunk_overlap = int(overlap_raw)
    except ValueError:
        chunk_overlap = 80

    return ChromaSettings(
        host=host,
        port=port,
        ssl=ssl,
        collection=collection,
        top_k=top_k,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )


def get_kimi_settings() -> KimiSettings:
    base_url = os.getenv("KIMI_BASE_URL", "https://api.moonshot.cn/v1").strip().rstrip("/")
    api_key = os.getenv("KIMI_API_KEY", "").strip()
    model = os.getenv("KIMI_MODEL", "moonshot-v1-8k").strip() or "moonshot-v1-8k"

    temp_raw = os.getenv("KIMI_TEMPERATURE", "0.2").strip()
    try:
        temperature = float(temp_raw)
    except ValueError:
        temperature = 0.2

    top_p_raw = os.getenv("KIMI_TOP_P", "0.9").strip()
    try:
        top_p = float(top_p_raw)
    except ValueError:
        top_p = 0.9

    max_tokens_raw = os.getenv("KIMI_MAX_TOKENS", "1024").strip()
    try:
        max_tokens = int(max_tokens_raw)
    except ValueError:
        max_tokens = 1024

    timeout_raw = os.getenv("KIMI_TIMEOUT_SECONDS", "60").strip()
    try:
        timeout_seconds = int(timeout_raw)
    except ValueError:
        timeout_seconds = 60

    if not api_key:
        raise ValueError("KIMI_API_KEY is required.")

    return KimiSettings(
        base_url=base_url,
        api_key=api_key,
        model=model,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        timeout_seconds=timeout_seconds,
    )


def get_siliconflow_settings() -> SiliconFlowSettings:
    base_url = os.getenv("SILICONFLOW_BASE_URL", "https://api.siliconflow.cn/v1").strip().rstrip("/")
    api_key = os.getenv("SILICONFLOW_API_KEY", "").strip()
    embedding_model = os.getenv("SILICONFLOW_EMBEDDING_MODEL", "Qwen/Qwen3-VL-Embedding-8B").strip()
    rerank_model = os.getenv("SILICONFLOW_RERANK_MODEL", "BAAI/bge-reranker-v2-m3").strip()

    enabled_raw = os.getenv("SILICONFLOW_RERANK_ENABLED", "true").strip().lower()
    rerank_enabled = enabled_raw in {"1", "true", "yes", "on"}

    timeout_raw = os.getenv("SILICONFLOW_TIMEOUT_SECONDS", "60").strip()
    try:
        timeout_seconds = int(timeout_raw)
    except ValueError:
        timeout_seconds = 60

    if not api_key:
        raise ValueError("SILICONFLOW_API_KEY is required.")

    return SiliconFlowSettings(
        base_url=base_url,
        api_key=api_key,
        embedding_model=embedding_model,
        rerank_model=rerank_model,
        rerank_enabled=rerank_enabled,
        timeout_seconds=timeout_seconds,
    )
