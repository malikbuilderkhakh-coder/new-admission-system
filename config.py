import streamlit as st

MODEL_NAME = "groq/openai/gpt-oss-120b"

def get_groq_api_key() -> str:
    """Read the API key from Streamlit Community Cloud Secrets."""
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception as exc:
        raise RuntimeError(
            "GROQ_API_KEY is missing. In Streamlit Community Cloud, open your app's "
            "Settings → Secrets and add: GROQ_API_KEY = \"your_groq_api_key\""
        ) from exc

    if not api_key or not str(api_key).strip():
        raise RuntimeError("GROQ_API_KEY is empty. Add your valid Groq API key to Streamlit Secrets.")
    return str(api_key).strip()
