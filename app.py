import os
import json
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

HISTORY_FILE = Path("chat_history.json")

def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(messages):
    with open(HISTORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)

st.set_page_config(page_title="LLM Chat • OpenAI", page_icon="💬")
st.title("💬 OpenAI Chat with Prompt Templates")
st.caption("LangChain • ChatOpenAI + Persistent History")

@st.cache_resource(show_spinner=False)
def get_chain(model_name: str):
    model = ChatOpenAI(model=model_name)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Keep answers concise."),
        MessagesPlaceholder("history"),
        ("human", "{input}")
    ])
    return prompt | model

# Sidebar: model + clear history
model_name = st.sidebar.text_input("Model name", value=os.getenv("OPENAI_MODEL", "gpt-4o-mini"))

if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.messages = []
    if HISTORY_FILE.exists():
        HISTORY_FILE.unlink()
    st.rerun()

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = load_history()

chain = get_chain(model_name)

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    history = []
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            history.append(HumanMessage(content=msg["content"]))
        else:
            history.append(AIMessage(content=msg["content"]))

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = chain.invoke({"input": user_input, "history": history[:-1]})
            st.markdown(result.content)

    st.session_state.messages.append({"role": "assistant", "content": result.content})
    save_history(st.session_state.messages)
