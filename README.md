# LangGraph Knowledge Chatbot

This project provides a lightweight Markdown RAG knowledge-base chatbot built with FastAPI and LangGraph.

Current UI status:
- A built-in web chat page is served from `/`
- Chainlit is currently disabled
- The main backend API remains `POST /v1/tools/langgraph/run`

## Install

```bash
pip install -r requirements.txt
```

## Configure

Copy `.env.example` to `.env` and fill in the required values.

Common settings:
- `KB_DIR`: local FAISS index directory, default `.faiss`
- `KB_LIBRARY_DIR`: markdown source directory, default `app/library`
- `KB_COLLECTION`: FAISS collection name, default `ncap_library`
- `KB_TOP_K`: retrieval result count for each question, default `4`
- `KB_CHUNK_SIZE`: max characters per markdown chunk, default `900`
- `KB_CHUNK_OVERLAP`: overlapping characters between chunks, default `120`
- `KB_MIN_SCORE`: minimum hybrid retrieval score before fallback, default `0.35`
- `SILICONFLOW_API_KEY`: required for embedding and optional rerank
- `KIMI_API_KEY`: required for LLM answer generation
- `TOOL_API_KEY`: optional API protection key

## Build The Knowledge Base

Put markdown files in `app/library`, then run:

```bash
python app/index_library_faiss.py
```

Useful options:

```bash
python app/index_library_faiss.py --library-dir app/library --chunk-size 900 --chunk-overlap 120
```

By default the command rebuilds the FAISS index so repeated runs do not duplicate chunks. Use `--append` only when you intentionally want to append documents to the existing index.

You can also rebuild the index through the API:

```bash
curl -X POST http://localhost:8000/v1/knowledge/index \
  -H 'Content-Type: application/json' \
  -d '{"library_dir":"app/library","reset":true,"recursive":true}'
```

Check index status:

```bash
curl http://localhost:8000/v1/knowledge/status
```

## Start The Service

```bash
uvicorn app.api:app --host 0.0.0.0 --port 8000
```

Or:

```bash
python server.py
```

Then open:

```text
http://localhost:8000/
```

Useful endpoints:
- `GET /`
- `GET /health`
- `GET /v1/knowledge/status`
- `POST /v1/knowledge/index`
- `POST /v1/tools/langgraph/run`
- `POST /v1/tools/langgraph/stream`
- `GET /docs`
- `GET /openapi.json`

## Request Example

```json
{
  "query": "Please summarize the key test conditions for NCAP low speed collisions.",
  "conversation_id": "",
  "strategy": "llm"
}
```

Supported strategies:
- `llm` / `rag`: retrieve markdown chunks, send them to the LLM node, and return an answer with sources
- `kb`: direct knowledge-base retrieval
- `checklist`: structured checklist-style answer

## Docker

```bash
docker compose -f docker-compose.prod.yml up -d --build
docker compose -f docker-compose.prod.yml logs -f api
curl http://localhost:8000/health
```

The production compose file now starts only the API service, and the chatbot page is included in that same service.
