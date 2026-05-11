from typing import Any, Dict

import requests

from app.config import get_settings


class DifyClient:
    def __init__(self) -> None:
        self.settings = get_settings()

    def chat(self, query: str, conversation_id: str = "") -> Dict[str, Any]:
        url = f"{self.settings.base_url}/v1/chat-messages"

        payload = {
            "inputs": {},
            "query": query,
            "response_mode": "blocking",
            "conversation_id": conversation_id,
            "user": self.settings.user,
        }
        headers = {
            "Authorization": f"Bearer {self.settings.api_key}",
            "Content-Type": "application/json",
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=self.settings.timeout_seconds,
        )

        response.raise_for_status()
        data = response.json()
        return {
            "answer": data.get("answer", ""),
            "conversation_id": data.get("conversation_id", ""),
            "raw": data,
        }
