"""Streamlit UI for the AI Utility Agent.

This front end keeps the original assistant behavior but presents it in a chat
interface. The backend still runs through the LangChain agent defined in
`agent.py`, so the UI is just a new presentation layer, not a rewrite.
"""

from __future__ import annotations

from uuid import uuid4

import streamlit as st

from agent import run_agent


st.set_page_config(page_title="AI Utility Agent", page_icon="🤖", layout="centered")

if "session_id" not in st.session_state:
    st.session_state.session_id = uuid4().hex

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask me to calculate, summarize, or use the mock weather and email tools.",
        }
    ]


def reset_chat() -> None:
    """Clear the chat history and start a fresh Streamlit session conversation."""

    st.session_state.session_id = uuid4().hex
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Chat reset. What would you like to do next?",
        }
    ]


st.sidebar.title("AI Utility Agent")
st.sidebar.write("LangChain-powered assistant with calculator, weather, email, and summarizer tools.")
st.sidebar.button("Reset chat", on_click=reset_chat)
st.sidebar.caption(f"Session: {st.session_state.session_id[:8]}")

st.title("AI Utility Agent")
st.caption("A simple Streamlit chat UI built on top of the LangChain agent.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type a message and press Enter")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_agent(user_input, session_id=st.session_state.session_id)
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})