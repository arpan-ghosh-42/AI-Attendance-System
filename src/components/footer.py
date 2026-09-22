import streamlit as st


def footer_home():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;">Made by Arpan Ghosh</p>
        </div>

                """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;">Made by Arpan Ghosh</p>
        </div>

                """, unsafe_allow_html=True)
