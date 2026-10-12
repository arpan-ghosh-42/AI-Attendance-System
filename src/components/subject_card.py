import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div class="snap-subject-card">
        <h3 class="snap-subject-title">{name}</h3>
        <p style="color:#5B5680; margin:10px 0;">Code : <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px; font-weight:600;">{code} </span> | Section : {section}</p>

        """

    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: #EB459E14; color:#14102E; padding:5px 12px; border-radius:12px; font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'

        html+= "</div>"

    html += "</div>"

    st.markdown("""
        <style>
            .snap-subject-card {
                background: rgba(253, 253, 255, 0.97);
                border-left: 8px solid #EB459E;
                padding: 25px;
                border-radius: 20px;
                border-top: 1px solid rgba(20, 16, 46, 0.08);
                border-right: 1px solid rgba(20, 16, 46, 0.08);
                border-bottom: 1px solid rgba(20, 16, 46, 0.08);
                margin-bottom: 20px;
                box-shadow: 0 8px 30px rgba(0, 0, 0, 0.25);
                transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            }
            .snap-subject-card:hover {
                transform: translateY(-6px);
                box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35), 0 0 30px rgba(139, 92, 246, 0.35);
            }
            .stApp .snap-subject-card h3.snap-subject-title {
                margin: 0 !important;
                font-size: 1.5rem !important;
                color: #14102E !important;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
