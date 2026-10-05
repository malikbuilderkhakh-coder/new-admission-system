import streamlit as st

MODEL_NAME = "groq/openai/gpt-oss-120b"

def get_groq_api_key() -> str:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception as exc:
        raise RuntimeError(
            'GROQ_API_KEY is missing. Add it in Streamlit Secrets as GROQ_API_KEY = "your_api_key".'
        ) from exc
    if not api_key or not str(api_key).strip():
        raise RuntimeError("GROQ_API_KEY is empty.")
    return str(api_key).strip()
