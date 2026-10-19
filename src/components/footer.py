import streamlit as st


def _footer(color):
    st.markdown(f"""
        <div style="margin-top:3rem; padding-top:1.2rem; border-top:1px solid rgba(34,211,238,0.15); display:flex; justify-content:center;">
        <p style="font-weight:600; color:{color}; opacity:0.85; font-size:0.9rem; letter-spacing:0.03em;">
            Made with <span style="color:#E879F9;">♥</span> by Arpan Ghosh
        </p>
        </div>
    """, unsafe_allow_html=True)


def footer_home():
    _footer("#D6E2F5")


def footer_dashboard():
    _footer("#9FB0D0")
