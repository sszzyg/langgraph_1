from app.workflow import build_graph


def main() -> None:
    graph = build_graph()

    print("LangGraph + Dify workflow is ready.")
    print("Type your question and press Enter (empty input to exit).")

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            print("Bye.")
            break

        result = graph.invoke({"input": user_input})
        print(f"Assistant: {result.get('answer', '')}")


if __name__ == "__main__":
    main()
