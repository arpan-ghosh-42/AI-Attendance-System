import threading

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Attendly - AI Attendance System",
    page_icon=Image.open("assets/images/logo.webp"),
    layout="centered",
)


@st.cache_resource(show_spinner=False)
def _preload_screens():
    # once per server process: import the heavy screens in the background
    # while the visitor is still on the home page, so the first click is instant
    def _load():
        import src.screens.teacher_screen  # noqa: F401
        import src.screens.student_screen  # noqa: F401
    threading.Thread(target=_load, daemon=True).start()
    return True


def main():

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    if st.query_params.get('join-code'):
        st.session_state['login_type'] = 'student'

    # screens are imported on demand: the teacher/student screens pull in
    # supabase, pandas and dlib, which is slow on a small free-tier instance
    match st.session_state['login_type']:
        case 'teacher':
            from src.screens.teacher_screen import teacher_screen
            teacher_screen()

        case 'student':
            from src.screens.student_screen import student_screen
            student_screen()

        case None:
            from src.screens.home_screen import home_screen
            home_screen()
            _preload_screens()

main()
