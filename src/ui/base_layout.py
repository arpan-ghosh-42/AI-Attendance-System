import streamlit as st
from src.ui.assets import image_data_uri


def _neon_background_css():
    bg_uri = image_data_uri("background.jpg")
    return f"""
        .stApp {{
            background: linear-gradient(180deg, rgba(8,8,32,0.55) 0%, rgba(8,8,32,0.75) 100%), url('{bg_uri}') !important;
            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
        }}
    """


def style_background_home():
    st.markdown(f"""
        <style>
            {_neon_background_css()}

            .stApp div[data-testid="stColumn"] {{
                background: linear-gradient(160deg, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0.04) 100%) !important;
                backdrop-filter: blur(20px) !important;
                -webkit-backdrop-filter: blur(20px) !important;
                border: 1px solid rgba(255,255,255,0.18) !important;
                padding: 2.5rem !important;
                border-radius: 2rem !important;
                box-shadow: 0 8px 32px rgba(0,0,0,0.35) !important;
                text-align: center !important;
                transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out, border-color 0.25s ease-in-out !important;
            }}
            .stApp div[data-testid="stColumn"]:hover {{
                transform: translateY(-10px) !important;
                border-color: rgba(139, 92, 246, 0.55) !important;
                box-shadow: 0 20px 50px rgba(0,0,0,0.45), 0 0 45px rgba(139, 92, 246, 0.3) !important;
            }}
            .stApp div[data-testid="stColumn"] div[data-testid="stVerticalBlock"] {{
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
            }}
            .stApp div[data-testid="stColumn"] h2 {{
                color: #F5F5FF !important;
                white-space: nowrap !important;
            }}
            .stApp div[data-testid="stColumn"] img {{
                display: block !important;
                margin: 0.5rem auto !important;
            }}
            .portal-subtext {{
                color: #C9CCFF !important;
                font-size: 0.95rem !important;
                margin: 0.4rem 0 1.5rem 0 !important;
            }}

            .snap-chip {{
                padding: 0.45rem 1rem;
                border-radius: 999px;
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.18);
                color: #F1F2FF;
                font-family: 'Outfit', sans-serif;
                font-size: 0.92rem;
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
            }}

            .st-key-student_portal_btn button {{
                background: linear-gradient(90deg, #5865F2 0%, #9B6BF6 100%) !important;
            }}
            .st-key-teacher_portal_btn button {{
                background: linear-gradient(90deg, #FF7A59 0%, #EB459E 100%) !important;
            }}
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown(f"""
        <style>
            {_neon_background_css()}

            /* centered content column - wide enough for 3 tabs + tables */
            .block-container {{
                max-width: 980px !important;
            }}

            /* metric cards */
            .stApp [data-testid="stMetric"] {{
                background: linear-gradient(160deg, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0.04) 100%);
                border: 1px solid rgba(255,255,255,0.16);
                border-radius: 1.2rem;
                padding: 1.1rem 1.4rem;
                backdrop-filter: blur(14px);
                -webkit-backdrop-filter: blur(14px);
                box-shadow: 0 6px 24px rgba(0,0,0,0.25);
            }}
            .stApp [data-testid="stMetricValue"] {{
                font-family: 'Climate Crisis', sans-serif !important;
                background: linear-gradient(90deg, #8B5CF6 0%, #EB459E 100%);
                -webkit-background-clip: text;
                background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            .stApp [data-testid="stMetricLabel"] p {{
                color: #C9CCFF !important;
            }}

            /* tables */
            .stApp [data-testid="stDataFrame"] {{
                border: 1px solid rgba(255,255,255,0.14);
                border-radius: 1rem;
                overflow: hidden;
                box-shadow: 0 6px 24px rgba(0,0,0,0.25);
            }}

            /* select boxes */
            .stApp [data-baseweb="select"] > div {{
                background: rgba(255, 255, 255, 0.06) !important;
                border: 1.5px solid rgba(255, 255, 255, 0.15) !important;
                border-radius: 0.9rem !important;
                transition: all 0.2s ease-in-out !important;
            }}
            .stApp [data-baseweb="select"] > div:hover {{
                border-color: rgba(139, 92, 246, 0.5) !important;
            }}

            /* alerts */
            .stApp [data-testid="stAlert"] {{
                border-radius: 1rem !important;
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.12);
            }}

            /* camera / file inputs */
            .stApp [data-testid="stFileUploaderDropzone"],
            .stApp [data-testid="stCameraInput"] {{
                background: rgba(255,255,255,0.05) !important;
                border: 1.5px dashed rgba(139, 92, 246, 0.5) !important;
                border-radius: 1rem !important;
            }}

            /* dialogs */
            div[role="dialog"] {{
                background: linear-gradient(160deg, rgba(30,24,86,0.97) 0%, rgba(14,12,52,0.98) 100%) !important;
                border: 1px solid rgba(139, 92, 246, 0.35) !important;
                border-radius: 1.5rem !important;
                box-shadow: 0 24px 80px rgba(0,0,0,0.6), 0 0 60px rgba(139,92,246,0.18) !important;
            }}

            /* dividers */
            .stApp hr {{
                border-color: rgba(255,255,255,0.12) !important;
            }}

            /* light titles + labels on the dark neon background */
            .stApp h1, .stApp h2, .stApp h3 {{
                color: #F5F5FF !important;
            }}
            .stApp h2 {{
                position: relative !important;
                display: inline-block !important;
                padding-bottom: 0.4rem !important;
            }}
            .stApp h2::after {{
                content: "" !important;
                position: absolute !important;
                left: 0 !important;
                bottom: 0 !important;
                width: 3rem !important;
                height: 4px !important;
                border-radius: 4px !important;
                background: linear-gradient(90deg, #8B5CF6 0%, #EB459E 100%) !important;
            }}
            .stApp [data-testid="stWidgetLabel"] p {{
                color: #C9CCFF !important;
                font-weight: 600 !important;
            }}

            /* text inputs */
            .stApp [data-testid="stTextInputRootElement"] {{
                background: rgba(255, 255, 255, 0.06) !important;
                border: 1.5px solid rgba(255, 255, 255, 0.15) !important;
                border-radius: 0.9rem !important;
                transition: all 0.2s ease-in-out !important;
            }}
            .stApp [data-testid="stTextInputRootElement"]:hover {{
                border-color: rgba(139, 92, 246, 0.5) !important;
            }}
            .stApp [data-testid="stTextInputRootElement"]:focus-within {{
                border-color: #8B5CF6 !important;
                box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.25) !important;
                transform: translateY(-1px);
            }}
            .stApp [data-testid="stTextInput"] input {{
                color: #F5F5FF !important;
                background: transparent !important;
            }}

            /* password strength meter */
            .pw-meter {{
                display: flex;
                gap: 6px;
                align-items: center;
                margin: -0.25rem 0 0.5rem 0;
                font-family: 'Outfit', sans-serif;
                font-size: 0.85rem;
                color: #C9CCFF;
            }}
            .pw-meter .seg {{
                flex: 1;
                height: 6px;
                border-radius: 4px;
                background: rgba(255, 255, 255, 0.12);
                transition: background 0.25s ease-in-out;
            }}
            .pw-meter .label {{
                min-width: 4.5rem;
                text-align: right;
                font-weight: 600;
            }}
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
            color: #F5F5FF;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 1.5rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
            color: #F5F5FF;
        }

        h3, h4, p {
            font-family: 'Outfit', sans-serif !important;
        }

        button {
            border-radius: 1.5rem !important;
            background: linear-gradient(90deg, #5865F2 0%, #9B6BF6 100%) !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
        }

        button[kind='secondary'] {
            border-radius: 1.5rem !important;
            background: linear-gradient(90deg, #EB459E 0%, #FF7A59 100%) !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
        }

        button[kind='tertiary'] {
            border-radius: 1.5rem !important;
            background: rgba(255, 255, 255, 0.06) !important;
            border: 1.5px solid rgba(255, 90, 120, 0.4) !important;
            color: #FF8FA3 !important;
            padding: 10px 20px !important;
            transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
        }
        button:hover{
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 8px 24px rgba(139, 92, 246, 0.4) !important;
        }
        button:active{
            transform: translateY(0) scale(0.98);
        }
        button:disabled{
            opacity: 0.4 !important;
            filter: grayscale(0.4);
        }
        button:disabled:hover{
            transform: none;
            box-shadow: none !important;
        }
        button p {
            font-weight: 600 !important;
            font-family: 'Outfit', sans-serif !important;
        }

        /* page fade-in */
        @keyframes snap-fade-up {
            from { opacity: 0; transform: translateY(14px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .block-container {
            animation: snap-fade-up 0.5s ease-out both;
        }

        /* gradient text helper + pill badge */
        .snap-gradient-text {
            background: linear-gradient(90deg, #8B5CF6 0%, #EB459E 55%, #FF7A59 100%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .snap-badge {
            display: inline-block;
            padding: 0.3rem 0.9rem;
            border-radius: 999px;
            background: rgba(139, 92, 246, 0.18);
            border: 1px solid rgba(139, 92, 246, 0.45);
            color: #D9CCFF;
            font-family: 'Outfit', sans-serif;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.04em;
        }

        /* scrollbar + selection */
        ::selection { background: rgba(139, 92, 246, 0.55); color: white; }
        ::-webkit-scrollbar { width: 10px; height: 10px; }
        ::-webkit-scrollbar-thumb { background: rgba(139, 92, 246, 0.45); border-radius: 8px; }
        ::-webkit-scrollbar-track { background: rgba(255,255,255,0.04); }

        @media (max-width: 640px) {
            h1 { font-size: 2.2rem !important; }
        }

        </style>
    """, unsafe_allow_html=True)
