import streamlit as st
from src.ui.assets import image_data_uri


def header_home():
    logo_uri = image_data_uri("logo.webp")

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:10px; margin-top:20px">
            <img src='{logo_uri}' style='height:clamp(120px, 32vw, 220px); width:auto; max-width:80vw; filter: drop-shadow(0 0 28px rgba(34, 211, 238, 0.35));' />
        </div>
                """, unsafe_allow_html=True)


def header_dashboard():
    logo_uri = image_data_uri("logo.webp")

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center;">
            <img src='{logo_uri}' style='height:clamp(60px, 14vw, 90px); width:auto; max-width:60vw;' />
        </div>
                """, unsafe_allow_html=True)
