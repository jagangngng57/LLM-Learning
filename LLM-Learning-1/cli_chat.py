# filepath: /LLM-Learning/LLM-Learning/cli_chat.py
import os
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

HISTORY_FILE = Path("chat_history.json")

def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as f:
            data = json.load(f)
            return [
                HumanMessage(content=msg["content"]) if msg["role"] == "user" else AIMessage(content=msg["content"])
                for msg in data
            ]
    return []

def save_history(history):
    data = []
    for msg in history:
        role = "user" if isinstance(msg, HumanMessage) else "assistant"
        data.append({"role": role, "content": msg.content})
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def build_chain(model_name: str):
    model = ChatOpenAI(model=model_name or os.getenv("OPENAI_MODEL", "gpt-4o-mini"))
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Keep answers concise."),
        MessagesPlaceholder("history"),
        ("human", "{input}")
    ])
    return prompt | model

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Simple OpenAI chat with persistent history.")
    parser.add_argument("--model", default=None, help="OpenAI model name, e.g. gpt-4o-mini")
    args = parser.parse_args()

    chain = build_chain(args.model)
    history = load_history()

    print(f"Model: {args.model or os.getenv('OPENAI_MODEL', 'gpt-4o-mini')}")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user = input("you > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nbye!")
            break
        if user.lower() in {"exit", "quit"}:
            print("bye!")
            break

        result = chain.invoke({"input": user, "history": history})
        print(f"bot > {result.content}\n")

        history.extend([HumanMessage(content=user), AIMessage(content=result.content)])
        save_history(history)

if __name__ == "__main__":
    main()