#!/usr/bin/env python3
"""Index markdown documents from app/library into FAISS knowledge base."""

from app.faiss_kb import FAISSKnowledgeBase


def main():
    kb = FAISSKnowledgeBase()
    print("Indexing documents from app/library...")
    result = kb.index_library()
    print(f"✅ Indexing complete: {result}")


if __name__ == "__main__":
    main()
