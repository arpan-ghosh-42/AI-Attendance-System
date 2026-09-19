import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #5865F2 0%, #7C6FF2 45%, #9B6BF6 100%) !important;
                background-attachment: fixed !important;
            }
            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 2.5rem !important;
                box-shadow: 0 12px 30px rgba(30, 20, 90, 0.35) !important;
                text-align: center !important;
                transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
            }
            .stApp div[data-testid="stColumn"]:hover {
                transform: translateY(-8px) !important;
                box-shadow: 0 18px 40px rgba(30, 20, 90, 0.45) !important;
            }
            .stApp div[data-testid="stColumn"] div[data-testid="stVerticalBlock"] {
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
            }
            .stApp div[data-testid="stColumn"] h2 {
                color: #262151 !important;
                white-space: nowrap !important;
            }
            .stApp div[data-testid="stColumn"] img {
                display: block !important;
                margin: 0.5rem auto !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #663399 !important;
            }
            
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@100..900&display=swap');

        /* HIDE THE TOP BAR OF STREAMLIT */

        #MainMenu, header, footer {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;
        }

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: #E0E3FF;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 1.5rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
            color: #E0E3FF;
        }

        h3, h4, p {
            font-family: 'Outfit', sans-serif !important;
        }

        button {
            border-radius: 1.5rem !important;
            background: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind='secondary'] {
            border-radius: 1.5rem !important;
            background: #EB459E !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind='tertiary'] {
            border-radius: 1.5rem !important;
            background: black !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }
        button:hover{
            transform: scale(1.05)
        }

        </style>
    """, unsafe_allow_html=True)