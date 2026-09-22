import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div class="snap-subject-card">
        <h3 style="margin:0; color: #14102E; font-size: 1.5rem ">{name}</h3>
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
                background: #FDFDFF;
                border-left: 8px solid #EB459E;
                padding: 25px;
                border-radius: 20px;
                border-top: 1px solid rgba(20, 16, 46, 0.08);
                border-right: 1px solid rgba(20, 16, 46, 0.08);
                border-bottom: 1px solid rgba(20, 16, 46, 0.08);
                margin-bottom: 20px;
                transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            }
            .snap-subject-card:hover {
                transform: translateY(-4px);
                box-shadow: 0 12px 24px rgba(30, 20, 90, 0.15);
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
