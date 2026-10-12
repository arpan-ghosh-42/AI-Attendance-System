import base64
import mimetypes
import streamlit as st

ASSETS_DIR = "assets/images"


@st.cache_data
def image_data_uri(filename):
    path = f"{ASSETS_DIR}/{filename}"
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:{mime};base64,{encoded}"
