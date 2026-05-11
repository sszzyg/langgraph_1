# LangGraph Knowledge Chatbot

This project provides a lightweight knowledge-base chatbot built with FastAPI and LangGraph.

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
- `TOOL_API_KEY`: optional API protection key

## Build The Knowledge Base

Put markdown files in `app/library`, then run:

```bash
python app/index_library_faiss.py
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
- `POST /v1/tools/langgraph/run`
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
- `llm`: retrieval plus natural-language answer
- `kb`: direct knowledge-base retrieval
- `checklist`: structured checklist-style answer

## Docker

```bash
docker compose -f docker-compose.prod.yml up -d --build
docker compose -f docker-compose.prod.yml logs -f api
curl http://localhost:8000/health
```

The production compose file now starts only the API service, and the chatbot page is included in that same service.
