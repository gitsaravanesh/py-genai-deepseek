import streamlit as st
import requests

st.title("DeepSeek Chat UI")
prompt = st.text_input("Enter your prompt:")

if st.button("Send"):
    payload = {
        "model": "deepseek-coder:1.3b-instruct",
        "prompt": prompt,
        "stream": False
    }
    resp = requests.post("http://127.0.0.1:11434/api/generate", json=payload)
    if resp.ok:
        data = resp.json()
        st.text_area("Response", data.get("response", ""), height=200)
    else:
        st.error(f"Error {resp.status_code}: {resp.text}")
