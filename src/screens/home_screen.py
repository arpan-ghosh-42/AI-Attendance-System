import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.ui.assets import image_data_uri
def home_screen():


    header_home()
    style_background_home()
    style_base_layout()

    st.markdown("""
        <div style="text-align:center; margin-bottom:0.8rem;">
            <span class="snap-badge">✨ AI-POWERED ATTENDANCE</span>
        </div>
        <p style="text-align:center; color:#E4E6FF; font-size:1.25rem; max-width:640px; margin:0 auto 1.2rem auto; line-height:1.5;">
            Take attendance in <span class="snap-gradient-text" style="font-weight:700;">seconds</span>
            using face and voice recognition for smarter, faster and easier classrooms.
        </p>
        <div style="display:flex; justify-content:center; gap:0.7rem; flex-wrap:wrap; margin:0 auto 2.5rem auto;">
            <span class="snap-chip">📸 Face recognition</span>
            <span class="snap-chip">🎙️ Voice recognition</span>
            <span class="snap-chip">📊 Instant reports</span>
            <span class="snap-chip">🔗 Join with a code</span>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(f"""
            <div style="display:flex; justify-content:center;">
                <img src="{image_data_uri('student_character.webp')}" style="width:150px; filter: drop-shadow(0 8px 24px rgba(88,101,242,0.5));" />
            </div>
        """, unsafe_allow_html=True)
        st.header("I'm a Student")
        st.markdown('<p class="portal-subtext">Register with your face, add your voice and track your attendance.</p>', unsafe_allow_html=True)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch', key='student_portal_btn'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.markdown(f"""
            <div style="display:flex; justify-content:center;">
                <img src="{image_data_uri('teacher_character.webp')}" style="width:150px; filter: drop-shadow(0 8px 24px rgba(235,69,158,0.5));" />
            </div>
        """, unsafe_allow_html=True)
        st.header("I'm a Teacher")
        st.markdown('<p class="portal-subtext">Manage classes, take attendance, and view detailed reports.</p>', unsafe_allow_html=True)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch', key='teacher_portal_btn'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()
