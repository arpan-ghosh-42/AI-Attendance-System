import streamlit as st
from src.ui.assets import image_data_uri


def header_home():
    logo_uri = image_data_uri("logo.webp")

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:10px; margin-top:20px">
            <img src='{logo_uri}' style='height:220px; filter: drop-shadow(0 0 30px rgba(139, 92, 246, 0.45));' />
        </div>
                """, unsafe_allow_html=True)


def header_dashboard():
    logo_uri = image_data_uri("logo.webp")

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center;">
            <img src='{logo_uri}' style='height:90px;' />
        </div>
                """, unsafe_allow_html=True)
