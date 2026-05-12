#!/usr/bin/env python3
"""Index markdown documents into the FAISS knowledge base."""

import argparse

from app.config import get_rag_settings
from app.faiss_kb import FAISSKnowledgeBase


def main():
    settings = get_rag_settings()
    parser = argparse.ArgumentParser(description="Build or update the Markdown RAG FAISS index.")
    parser.add_argument("--library-dir", default=settings.library_dir, help="Directory containing markdown files.")
    parser.add_argument("--chunk-size", type=int, default=settings.chunk_size, help="Maximum characters per chunk.")
    parser.add_argument(
        "--chunk-overlap",
        type=int,
        default=settings.chunk_overlap,
        help="Overlapping characters between chunks.",
    )
    parser.add_argument(
        "--append",
        action="store_true",
        help="Append to the current index instead of rebuilding it.",
    )
    parser.add_argument(
        "--no-recursive",
        action="store_true",
        help="Only index markdown files directly under --library-dir.",
    )
    args = parser.parse_args()

    if args.chunk_overlap >= args.chunk_size:
        raise SystemExit("--chunk-overlap must be smaller than --chunk-size")

    kb = FAISSKnowledgeBase()
    print(f"Indexing markdown documents from {args.library_dir}...")
    result = kb.index_library(
        library_dir=args.library_dir,
        chunk_size=args.chunk_size,
        overlap=args.chunk_overlap,
        reset=not args.append,
        recursive=not args.no_recursive,
    )
    print(f"Indexing complete: {result}")


if __name__ == "__main__":
    main()
