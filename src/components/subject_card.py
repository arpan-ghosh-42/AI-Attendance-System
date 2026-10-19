import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div class="snap-subject-card">
        <h3 class="snap-subject-title">{name}</h3>
        <p style="color:#C9CCFF; margin:10px 0;">Code : <span style="background:rgba(139,92,246,0.25); border:1px solid rgba(139,92,246,0.5); color:#E4DAFF; padding:2px 10px; border-radius:999px; font-weight:600;">{code} </span> &nbsp;|&nbsp; Section : {section}</p>

        """

    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: rgba(235,69,158,0.16); border:1px solid rgba(235,69,158,0.35); color:#FFE3F1; padding:5px 12px; border-radius:12px; font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'

        html+= "</div>"

    html += "</div>"

    st.markdown("""
        <style>
            .snap-subject-card {
                background: linear-gradient(160deg, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0.04) 100%);
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                border-left: 6px solid #EB459E;
                padding: 25px;
                border-radius: 20px;
                border-top: 1px solid rgba(255, 255, 255, 0.16);
                border-right: 1px solid rgba(255, 255, 255, 0.16);
                border-bottom: 1px solid rgba(255, 255, 255, 0.16);
                margin-bottom: 20px;
                box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
                transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out, border-color 0.2s ease-in-out;
            }
            .snap-subject-card:hover {
                transform: translateY(-6px);
                border-left-color: #8B5CF6;
                box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4), 0 0 30px rgba(139, 92, 246, 0.35);
            }
            .stApp .snap-subject-card h3.snap-subject-title {
                margin: 0 !important;
                font-size: 1.5rem !important;
                color: #F5F5FF !important;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
