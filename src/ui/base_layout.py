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
            /* soft lavender -> pink background that slowly drifts */
            .stApp {
                background: linear-gradient(135deg, #E0E3FF 0%, #ECE4FF 45%, #FBE3F1 100%) !important;
                background-size: 200% 200% !important;
                animation: snapDrift 18s ease-in-out infinite;
            }
            @keyframes snapDrift {
                0%   { background-position: 0% 50%; }
                50%  { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            /* narrow, centered content column */
            .block-container {
                max-width: 640px !important;
            }

            /* dark titles + labels on the light background */
            .stApp h1, .stApp h2, .stApp h3 {
                color: #14102E !important;
            }
            .stApp h2 {
                position: relative !important;
                display: inline-block !important;
                padding-bottom: 0.4rem !important;
            }
            .stApp h2::after {
                content: "" !important;
                position: absolute !important;
                left: 0 !important;
                bottom: 0 !important;
                width: 3rem !important;
                height: 4px !important;
                border-radius: 4px !important;
                background: linear-gradient(90deg, #5865F2 0%, #EB459E 100%) !important;
            }
            .stApp h2.snap-logo-text {
                padding-bottom: 0 !important;
            }
            .stApp h2.snap-logo-text::after {
                content: none !important;
            }
            .st-key-dash_title h2 {
                font-size: 1.6rem !important;
                line-height: 1.15 !important;
                margin: 1rem 0 1.5rem 0 !important;
            }
            .stApp [data-testid="stWidgetLabel"] p {
                color: #262151 !important;
                font-weight: 600 !important;
            }

            /* text inputs */
            .stApp [data-testid="stTextInputRootElement"] {
                background: #F1F2FF !important;
                border: 1.5px solid transparent !important;
                border-radius: 0.9rem !important;
                transition: all 0.2s ease-in-out !important;
            }
            .stApp [data-testid="stTextInputRootElement"]:hover {
                border-color: #B9BEFA !important;
            }
            .stApp [data-testid="stTextInputRootElement"]:focus-within {
                border-color: #5865F2 !important;
                box-shadow: 0 0 0 4px rgba(88, 101, 242, 0.18) !important;
                transform: translateY(-1px);
            }
            .stApp [data-testid="stTextInput"] input {
                color: #262151 !important;
                background: transparent !important;
            }

            /* password strength meter */
            .pw-meter {
                display: flex;
                gap: 6px;
                align-items: center;
                margin: -0.25rem 0 0.5rem 0;
                font-family: 'Outfit', sans-serif;
                font-size: 0.85rem;
                color: #262151;
            }
            .pw-meter .seg {
                flex: 1;
                height: 6px;
                border-radius: 4px;
                background: #D3D6F5;
                transition: background 0.25s ease-in-out;
            }
            .pw-meter .label {
                min-width: 4.5rem;
                text-align: right;
                font-weight: 600;
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