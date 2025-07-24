import streamlit as st
import requests, json

MODEL = "deepseek-coder:1.3b-instruct"
API   = "http://127.0.0.1:11434/api/generate"

st.title("MY LLM")

if 'history' not in st.session_state:
    st.session_state.history = []

prompt = st.text_area("Your prompt:", height=120)

if st.button("Send"):
    payload = {"model": MODEL, "prompt": prompt, "stream": False}
    r = requests.post(API, json=payload)
    r.raise_for_status()
    reply = r.json().get("response", "")
    st.session_state.history.append(("You", prompt))
    st.session_state.history.append(("AI", reply))

for who, text in st.session_state.history[::-1]:
    st.markdown(f"**{who}:** {text}")
