from app.kb import ChromaKnowledgeBase


def main() -> None:
    kb = ChromaKnowledgeBase()
    result = kb.index_library()
    print("Chroma index finished.")
    print(f"Collection: {result['collection']}")
    print(f"Files: {result['files']}")
    print(f"Chunks: {result['chunks']}")
    print(f"Folder: {result['folder']}")


if __name__ == "__main__":
    main()
