import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

# tiny inline icons (a few hundred bytes) instead of ~90KB of character images
_STUDENT_ICON = """
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M3 8V5.5A2.5 2.5 0 0 1 5.5 3H8M16 3h2.5A2.5 2.5 0 0 1 21 5.5V8M21 16v2.5a2.5 2.5 0 0 1-2.5 2.5H16M8 21H5.5A2.5 2.5 0 0 1 3 18.5V16"/>
    <circle cx="12" cy="10" r="3.2"/>
    <path d="M6.8 18c1.1-2.4 3-3.6 5.2-3.6s4.1 1.2 5.2 3.6"/>
</svg>
"""

_TEACHER_ICON = """
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M2.5 4h19"/>
    <path d="M4 4v10.5A1.5 1.5 0 0 0 5.5 16h13a1.5 1.5 0 0 0 1.5-1.5V4"/>
    <path d="M12 16v3.5M8.5 21.5 12 19.5l3.5 2"/>
    <path d="m7.5 12 3-3.2 2.4 2.2 3.6-4"/>
</svg>
"""


def _go(login_type):
    st.session_state['login_type'] = login_type


def home_screen():


    header_home()
    style_background_home()
    style_base_layout()

    st.markdown("""
        <div style="text-align:center; margin-bottom:1rem;">
            <span class="snap-badge"><span class="dot"></span>AI-POWERED ATTENDANCE</span>
        </div>
        <p class="snap-tagline" style="text-align:center; color:#D6E2F5; font-size:1.25rem; max-width:640px; margin:0 auto 1.2rem auto; line-height:1.5;">
            Take attendance in <span class="snap-gradient-text" style="font-weight:700;">seconds</span>
            using face and voice recognition for smarter, faster and easier classrooms.
        </p>
        <div style="display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap; margin:0 auto 2.5rem auto;">
            <span class="snap-chip">📸 Face recognition</span>
            <span class="snap-chip">🎙️ Voice recognition</span>
            <span class="snap-chip">📊 Instant reports</span>
            <span class="snap-chip">🔗 Join with a code</span>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(f'<div class="snap-orb cyan">{_STUDENT_ICON}</div>', unsafe_allow_html=True)
        st.header("I'm a Student")
        st.markdown('<p class="portal-subtext">Register with your face, add your voice and track your attendance.</p>', unsafe_allow_html=True)
        st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch', key='student_portal_btn',
                  on_click=_go, args=('student',))

    with col2:
        st.markdown(f'<div class="snap-orb magenta">{_TEACHER_ICON}</div>', unsafe_allow_html=True)
        st.header("I'm a Teacher")
        st.markdown('<p class="portal-subtext">Manage classes, take attendance, and view detailed reports.</p>', unsafe_allow_html=True)
        st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch', key='teacher_portal_btn',
                  on_click=_go, args=('teacher',))

    footer_home()
