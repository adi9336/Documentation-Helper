from typing import Set

from backend.core import run_llm

import streamlit as st

st.header("Documentation Helper Bot")

prompt = st.text_input("Prompt", placeholder="Enter your prompt here..")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []


def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"- {source}\n"
    return sources_string

# The output appears twice because:
# 1. st.write(generated_response["answer"]) displays the answer immediately after generation.
# 2. Later, in the chat history loop, st.chat_message("assistant").write(generated_response) displays the formatted response (which includes the answer again).
# So, the answer is shown once directly and once as part of the chat history.

if prompt:
    with st.spinner("Generating response.."):
        generated_response = run_llm(query=prompt)
        # Expecting generated_response to be a dict with keys "answer" and "context"
        # "answer" is the string answer, "context" is a list of documents with .metadata["source"]
        # st.write(generated_response["answer"])  # This line causes the answer to be shown immediately
        # Safely get sources from context if available
        sources = set()
        if "context" in generated_response and generated_response["context"]:
            sources = set(
                [doc.metadata["source"] for doc in generated_response["context"] if "source" in doc.metadata]
            )

        formatted_response = (
            f"{generated_response['answer']} \n\n {create_sources_string(sources)}"
        )

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)

if st.session_state["chat_answers_history"]:
    for user_query, generated_response in zip(
        st.session_state["user_prompt_history"],
        st.session_state["chat_answers_history"],
    ):
        st.chat_message("user").write(user_query)
        st.chat_message("assistant").write(generated_response)
