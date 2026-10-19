import streamlit as st

# Futuristic "holo-grid" theme. Everything is plain CSS: no background image,
# no backdrop blur and no looping animations, so pages stay light to paint.

_BACKGROUND = """
    .stApp {
        background: #05060F !important;
        isolation: isolate;
    }
    /* static grid + glow, on a fixed GPU layer so scrolling never repaints it */
    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        z-index: -1;
        pointer-events: none;
        background:
            radial-gradient(60rem 36rem at 8% -12%, rgba(34, 211, 238, 0.16), transparent 62%),
            radial-gradient(52rem 36rem at 105% 108%, rgba(217, 70, 239, 0.13), transparent 62%),
            linear-gradient(rgba(34, 211, 238, 0.055) 1px, transparent 1px) 0 0 / 46px 46px,
            linear-gradient(90deg, rgba(34, 211, 238, 0.055) 1px, transparent 1px) 0 0 / 46px 46px;
        transform: translateZ(0);
    }
    /* thin neon horizon line at the very top */
    .stApp::after {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        z-index: 1000;
        pointer-events: none;
        background: linear-gradient(90deg, transparent, #22D3EE 25%, #8B5CF6 55%, #D946EF 80%, transparent);
    }
"""

# shared look for every "HUD panel" (cards, metrics, home portals)
_PANEL = """
        background: linear-gradient(160deg, rgba(17, 24, 52, 0.92) 0%, rgba(9, 12, 30, 0.94) 100%) !important;
        border: 1px solid rgba(34, 211, 238, 0.18) !important;
        border-radius: 18px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
"""


def style_background_home():
    st.markdown("""
        <style>
            """ + _BACKGROUND + """

            .stApp div[data-testid="stColumn"] {
                """ + _PANEL + """
                position: relative;
                padding: 2.2rem !important;
                text-align: center !important;
                transition: transform 0.18s ease-out, border-color 0.18s ease-out !important;
            }
            /* neon accent bar on top of each portal card */
            .stApp div[data-testid="stColumn"]::before {
                content: "";
                position: absolute;
                top: -1px;
                left: 22%;
                right: 22%;
                height: 2px;
                border-radius: 2px;
                background: linear-gradient(90deg, transparent, #22D3EE, #D946EF, transparent);
            }
            @media (hover: hover) {
                .stApp div[data-testid="stColumn"]:hover {
                    transform: translateY(-6px) !important;
                    border-color: rgba(34, 211, 238, 0.45) !important;
                    box-shadow: 0 18px 44px rgba(0, 0, 0, 0.55), 0 0 32px rgba(34, 211, 238, 0.16) !important;
                }
            }
            .stApp div[data-testid="stColumn"] div[data-testid="stVerticalBlock"] {
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
            }
            .stApp div[data-testid="stColumn"] h2 {
                color: #F2F7FF !important;
                white-space: nowrap !important;
            }
            .stApp div[data-testid="stColumn"] [data-testid="stHeading"],
            .stApp div[data-testid="stColumn"] [data-testid="stMarkdownContainer"],
            .stApp div[data-testid="stColumn"] h2,
            .portal-subtext {
                width: 100% !important;
                text-align: center !important;
            }
            .portal-subtext {
                color: #9FB0D0 !important;
                font-size: 0.98rem !important;
                margin: 0.5rem 0 1.4rem 0 !important;
            }

            /* glowing icon ring that replaces the character images */
            .snap-orb {
                width: 104px;
                height: 104px;
                margin: 0.2rem auto 0.6rem auto;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                background: radial-gradient(circle at 50% 40%, rgba(255, 255, 255, 0.06), rgba(5, 6, 15, 0.9) 70%);
                border: 1.5px solid var(--orb);
                box-shadow: 0 0 0 6px rgba(255, 255, 255, 0.02), 0 0 28px var(--orb-glow), inset 0 0 18px var(--orb-glow);
                color: var(--orb);
            }
            .snap-orb svg { width: 50px; height: 50px; }
            .snap-orb.cyan { --orb: #22D3EE; --orb-glow: rgba(34, 211, 238, 0.35); }
            .snap-orb.magenta { --orb: #E879F9; --orb-glow: rgba(217, 70, 239, 0.35); }

            .snap-chip {
                padding: 0.42rem 0.95rem;
                border-radius: 8px;
                background: rgba(34, 211, 238, 0.06);
                border: 1px solid rgba(34, 211, 238, 0.22);
                color: #CFE9F5;
                font-family: 'Outfit', sans-serif;
                font-size: 0.9rem;
                letter-spacing: 0.02em;
            }

            .st-key-student_portal_btn button {
                background: linear-gradient(90deg, #06B6D4 0%, #6366F1 100%) !important;
            }
            .st-key-teacher_portal_btn button {
                background: linear-gradient(90deg, #8B5CF6 0%, #D946EF 100%) !important;
            }

            @media (max-width: 640px) {
                .stApp div[data-testid="stColumn"] {
                    padding: 1.5rem !important;
                }
                .stApp div[data-testid="stColumn"] h2 {
                    white-space: normal !important;
                }
                .snap-orb { width: 84px; height: 84px; }
                .snap-tagline { font-size: 1.05rem !important; }
                .snap-orb svg { width: 40px; height: 40px; }
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            """ + _BACKGROUND + """

            /* centered content column - wide enough for 3 tabs + tables */
            .block-container {
                max-width: 980px !important;
            }

            /* metric cards */
            .stApp [data-testid="stMetric"] {
                """ + _PANEL + """
                padding: 1.1rem 1.4rem;
            }
            .stApp [data-testid="stMetricValue"] {
                font-family: 'Orbitron', sans-serif !important;
                font-weight: 700 !important;
                color: #67E8F9 !important;
                text-shadow: 0 0 18px rgba(34, 211, 238, 0.35);
            }
            .stApp [data-testid="stMetricLabel"] p {
                color: #9FB0D0 !important;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                font-size: 0.8rem !important;
            }

            /* tables */
            .stApp [data-testid="stDataFrame"] {
                border: 1px solid rgba(34, 211, 238, 0.18);
                border-radius: 14px;
                overflow: hidden;
            }

            /* select boxes */
            .stApp [data-baseweb="select"] > div {
                background: rgba(9, 12, 30, 0.9) !important;
                border: 1px solid rgba(34, 211, 238, 0.2) !important;
                border-radius: 12px !important;
            }
            .stApp [data-baseweb="select"] > div:hover {
                border-color: rgba(34, 211, 238, 0.5) !important;
            }

            /* alerts */
            .stApp [data-testid="stAlert"] {
                border-radius: 12px !important;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }

            /* camera / file / audio inputs */
            .stApp [data-testid="stFileUploaderDropzone"],
            .stApp [data-testid="stCameraInput"] {
                background: rgba(9, 12, 30, 0.85) !important;
                border: 1px dashed rgba(34, 211, 238, 0.45) !important;
                border-radius: 14px !important;
            }

            /* bordered containers (e.g. registration form) */
            .stApp [data-testid="stVerticalBlockBorderWrapper"] {
                background: rgba(9, 12, 30, 0.7);
                border-color: rgba(34, 211, 238, 0.2) !important;
                border-radius: 16px !important;
            }

            /* dialogs */
            div[role="dialog"] {
                background: linear-gradient(160deg, #0F1630 0%, #080B1C 100%) !important;
                border: 1px solid rgba(34, 211, 238, 0.3) !important;
                border-radius: 18px !important;
                box-shadow: 0 24px 80px rgba(0, 0, 0, 0.7), 0 0 40px rgba(34, 211, 238, 0.12) !important;
            }

            /* dividers */
            .stApp hr {
                border: none !important;
                height: 1px !important;
                background: linear-gradient(90deg, transparent, rgba(34, 211, 238, 0.35), rgba(217, 70, 239, 0.35), transparent) !important;
            }

            /* titles + labels */
            .stApp h1, .stApp h2, .stApp h3 {
                color: #F2F7FF !important;
            }
            .stApp h2 {
                position: relative !important;
                display: inline-block !important;
                padding-bottom: 0.5rem !important;
            }
            .stApp h2::after {
                content: "" !important;
                position: absolute !important;
                left: 0 !important;
                bottom: 0 !important;
                width: 2.6rem !important;
                height: 3px !important;
                border-radius: 3px !important;
                background: linear-gradient(90deg, #22D3EE 0%, #D946EF 100%) !important;
                box-shadow: 0 0 10px rgba(34, 211, 238, 0.5);
            }
            .stApp [data-testid="stWidgetLabel"] p {
                color: #9FB0D0 !important;
                font-weight: 600 !important;
                letter-spacing: 0.02em;
            }

            /* text inputs */
            .stApp [data-testid="stTextInputRootElement"] {
                background: rgba(9, 12, 30, 0.9) !important;
                border: 1px solid rgba(34, 211, 238, 0.2) !important;
                border-radius: 12px !important;
                transition: border-color 0.15s ease-out !important;
            }
            .stApp [data-testid="stTextInputRootElement"]:hover {
                border-color: rgba(34, 211, 238, 0.45) !important;
            }
            .stApp [data-testid="stTextInputRootElement"]:focus-within {
                border-color: #22D3EE !important;
                box-shadow: 0 0 0 3px rgba(34, 211, 238, 0.2) !important;
            }
            .stApp [data-testid="stTextInput"] input {
                color: #F2F7FF !important;
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
                color: #9FB0D0;
            }
            .pw-meter .seg {
                flex: 1;
                height: 5px;
                border-radius: 4px;
                background: rgba(255, 255, 255, 0.1);
                transition: background 0.2s ease-out;
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

        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800&family=Outfit:wght@400;600;700&display=swap');

        /* HIDE THE TOP BAR OF STREAMLIT */

        #MainMenu, header, footer {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;
        }

        h1 {
            font-family: 'Orbitron', sans-serif !important;
            font-weight: 800 !important;
            font-size: 3.2rem !important;
            line-height: 1.1 !important;
            letter-spacing: 0.02em !important;
            margin-bottom: 0rem !important;
            color: #F2F7FF;
        }

        h2 {
            font-family: 'Orbitron', sans-serif !important;
            font-weight: 600 !important;
            font-size: 1.35rem !important;
            line-height: 1.15 !important;
            letter-spacing: 0.03em !important;
            margin-bottom: 0rem !important;
            color: #F2F7FF;
        }

        h3, h4, p, li, label {
            font-family: 'Outfit', sans-serif !important;
        }

        button {
            border-radius: 12px !important;
            background: linear-gradient(90deg, #06B6D4 0%, #6366F1 100%) !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.15s ease-out !important;
        }

        button[kind='secondary'] {
            background: linear-gradient(90deg, #8B5CF6 0%, #D946EF 100%) !important;
            color: white !important;
            border: none !important;
        }

        button[kind='tertiary'] {
            background: rgba(9, 12, 30, 0.85) !important;
            border: 1px solid rgba(159, 176, 208, 0.28) !important;
            color: #B9C6E4 !important;
        }
        @media (hover: hover) {
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 22px rgba(34, 211, 238, 0.25) !important;
            }
            button[kind='tertiary']:hover {
                border-color: rgba(34, 211, 238, 0.6) !important;
                color: #E6FBFF !important;
            }
        }
        button:active {
            transform: translateY(0) scale(0.98);
        }
        /* icon buttons inside inputs (password eye, number steppers) stay plain */
        [data-testid="stTextInputRootElement"] button,
        [data-testid="stNumberInputContainer"] button {
            background: transparent !important;
            padding: 0 10px !important;
            border-radius: 8px !important;
            box-shadow: none !important;
            transform: none !important;
            color: #9FB0D0 !important;
        }
        button:disabled {
            opacity: 0.4 !important;
            filter: grayscale(0.4);
        }
        button:disabled:hover {
            transform: none !important;
            box-shadow: none !important;
        }
        button p {
            font-weight: 600 !important;
            letter-spacing: 0.03em;
            font-family: 'Outfit', sans-serif !important;
        }

        /* page fade-in (opacity only, cheap) */
        @keyframes snap-fade-in {
            from { opacity: 0; }
            to   { opacity: 1; }
        }
        .block-container {
            animation: snap-fade-in 0.2s ease-out both;
        }

        /* gradient text helper + pill badge */
        .snap-gradient-text {
            background: linear-gradient(90deg, #22D3EE 0%, #8B5CF6 55%, #E879F9 100%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .snap-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.32rem 0.9rem;
            border-radius: 6px;
            background: rgba(34, 211, 238, 0.08);
            border: 1px solid rgba(34, 211, 238, 0.4);
            color: #A5F3FC;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.18em;
        }
        .snap-badge .dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #22D3EE;
            box-shadow: 0 0 8px #22D3EE;
        }

        /* scrollbar + selection */
        ::selection { background: rgba(34, 211, 238, 0.45); color: white; }
        ::-webkit-scrollbar { width: 9px; height: 9px; }
        ::-webkit-scrollbar-thumb { background: rgba(34, 211, 238, 0.35); border-radius: 8px; }
        ::-webkit-scrollbar-track { background: #05060F; }

        @media (max-width: 640px) {
            .block-container {
                padding: 1rem 1rem 3rem 1rem !important;
            }
            h1 { font-size: 2rem !important; }
            h2 { font-size: 1.1rem !important; }
            button { padding: 10px 14px !important; }
            /* stacked columns: don't keep the huge desktop gaps */
            [data-testid="stHorizontalBlock"] { gap: 1.6rem !important; }
            [data-testid="stMetricValue"] { font-size: 1.5rem !important; }
            [data-testid="stDataFrame"] { max-width: 100%; overflow-x: auto; }
            img { max-width: 100%; height: auto; }
        }

        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation: none !important;
                transition: none !important;
            }
        }

        </style>
    """, unsafe_allow_html=True)
