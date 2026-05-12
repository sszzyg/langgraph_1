import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import numpy as np

from app.faiss_kb import FAISSKnowledgeBase


class FakeEmbeddingKnowledgeBase(FAISSKnowledgeBase):
    def _embed(self, text: str) -> np.ndarray:
        vector = np.zeros(8, dtype="float32")
        for token in text.lower().split():
            vector[sum(ord(char) for char in token) % len(vector)] += 1.0
        if not vector.any():
            vector[0] = 1.0
        return self._l2_normalize(vector)


class FAISSKnowledgeBaseTest(unittest.TestCase):
    def test_split_markdown_keeps_heading_context(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with patch.dict(os.environ, {"KB_DIR": tmp, "SILICONFLOW_API_KEY": "test"}, clear=False):
                kb = FAISSKnowledgeBase(collection_name="split_test")

                chunks = kb._split_markdown(
                    "# Intro\nalpha beta\n\n## Details\n" + ("gamma " * 80),
                    chunk_size=120,
                    overlap=20,
                )

        self.assertGreaterEqual(len(chunks), 2)
        self.assertTrue(chunks[0].startswith("# Intro"))
        self.assertTrue(any(chunk.startswith("## Details") for chunk in chunks))

    def test_rebuild_index_does_not_duplicate_vectors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            kb_dir = Path(tmp) / "faiss"
            library_dir = Path(tmp) / "library"
            nested_dir = library_dir / "nested"
            nested_dir.mkdir(parents=True)
            (library_dir / "alpha.md").write_text("# Alpha\nalpha beta", encoding="utf-8")
            (nested_dir / "gamma.md").write_text("# Gamma\ngamma delta", encoding="utf-8")

            env = {
                "KB_DIR": str(kb_dir),
                "KB_COLLECTION": "unit_test",
                "KB_LIBRARY_DIR": str(library_dir),
                "KB_TOP_K": "2",
                "SILICONFLOW_API_KEY": "test",
                "SILICONFLOW_RERANK_ENABLED": "false",
            }
            with patch.dict(os.environ, env, clear=False):
                kb = FakeEmbeddingKnowledgeBase()
                first = kb.index_library(reset=True, chunk_size=200, overlap=20)
                first_vectors = kb.status()["vectors"]

                second = kb.index_library(reset=True, chunk_size=200, overlap=20)
                second_vectors = kb.status()["vectors"]

                hits = kb.query("alpha", top_k=1)

        self.assertEqual(first["files_indexed"], 2)
        self.assertEqual(second["files_indexed"], 2)
        self.assertEqual(first_vectors, second_vectors)
        self.assertEqual(first_vectors, 2)
        self.assertEqual(hits[0]["source"], "alpha.md")


if __name__ == "__main__":
    unittest.main()
