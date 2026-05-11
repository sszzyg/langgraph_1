import os
from typing import Any, Dict, List

import requests

from app.config import get_kimi_settings


class KimiClient:
    def __init__(self) -> None:
        self.settings = get_kimi_settings()

    def chat(self, query: str, context: str = "") -> str:
        url = f"{self.settings.base_url}/chat/completions"

        messages: List[Dict[str, str]] = [
            {
                "role": "system",
                "content": (
                    "你是一名专业的汽车主动安全测试工程师助手，精通 Euro NCAP、CNCAP 等碰撞安全与主动避撞测试协议。\n"
                    "请根据提供的知识库片段，用中文给出准确、结构清晰的回答。\n"
                    "回答时请注意：\n"
                    "1. 优先引用知识库中的具体数值、条件和标准；\n"
                    "2. 如果知识库片段不足以完整回答，请明确指出哪些信息缺失；\n"
                    "3. 不要编造知识库中没有的数据或标准；\n"
                    "4. 使用条目化、分层次的方式组织回答，便于阅读。"
                ),
            }
        ]

        if context:
            user_content = (
                "请根据以下知识库片段回答用户问题。\n\n"
                "【知识库片段】\n"
                f"{context}\n\n"
                "【用户问题】\n"
                f"{query}"
            )
        else:
            user_content = query

        messages.append({"role": "user", "content": user_content})

        payload = {
            "model": self.settings.model,
            "messages": messages,
            "temperature": self.settings.temperature,
            "top_p": self.settings.top_p,
            "max_tokens": self.settings.max_tokens,
        }

        headers = {
            "Authorization": f"Bearer {self.settings.api_key}",
            "Content-Type": "application/json",
        }

        response = requests.post(url, json=payload, headers=headers, timeout=self.settings.timeout_seconds)
        response.raise_for_status()
        data = response.json()
        return self._extract_answer(data)

    @staticmethod
    def _extract_answer(data: Dict[str, Any]) -> str:
        choices = data.get("choices") or []
        if not choices:
            return ""
        message = choices[0].get("message") or {}
        return (message.get("content") or "").strip()
