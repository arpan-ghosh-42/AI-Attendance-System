import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div class="snap-subject-card">
        <h3 class="snap-subject-title">{name}</h3>
        <p style="color:#9FB0D0; margin:10px 0;">Code : <span style="background:rgba(34,211,238,0.1); border:1px solid rgba(34,211,238,0.45); color:#A5F3FC; padding:2px 10px; border-radius:6px; font-weight:600; letter-spacing:0.05em;">{code} </span> &nbsp;|&nbsp; Section : {section}</p>

        """

    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: rgba(217,70,239,0.1); border:1px solid rgba(217,70,239,0.32); color:#F5D0FE; padding:5px 12px; border-radius:8px; font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'

        html+= "</div>"

    html += "</div>"

    st.markdown("""
        <style>
            .snap-subject-card {
                background: linear-gradient(160deg, rgba(17, 24, 52, 0.92) 0%, rgba(9, 12, 30, 0.94) 100%);
                border: 1px solid rgba(34, 211, 238, 0.18);
                border-left: 3px solid #22D3EE;
                padding: 24px;
                border-radius: 16px;
                margin-bottom: 20px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
                transition: transform 0.18s ease-out;
            }
            @media (hover: hover) {
                .snap-subject-card:hover {
                    transform: translateY(-5px);
                    border-color: rgba(34, 211, 238, 0.45);
                    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5), 0 0 26px rgba(34, 211, 238, 0.15);
                }
            }
            @media (max-width: 640px) {
                .snap-subject-card { padding: 18px; }
            }
            .stApp .snap-subject-card h3.snap-subject-title {
                margin: 0 !important;
                font-family: 'Orbitron', sans-serif !important;
                font-weight: 600 !important;
                font-size: 1.2rem !important;
                letter-spacing: 0.03em;
                color: #F2F7FF !important;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
