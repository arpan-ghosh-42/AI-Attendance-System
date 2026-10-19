import streamlit as st


def _footer(color):
    st.markdown(f"""
        <div style="margin-top:3rem; padding-top:1.2rem; border-top:1px solid rgba(255,255,255,0.1); display:flex; justify-content:center;">
        <p style="font-weight:600; color:{color}; opacity:0.85; font-size:0.9rem; letter-spacing:0.03em;">
            Made with <span style="color:#EB459E;">♥</span> by Arpan Ghosh
        </p>
        </div>
    """, unsafe_allow_html=True)


def footer_home():
    _footer("white")


def footer_dashboard():
    _footer("#C9CCFF")
