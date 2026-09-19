import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home

#streamlit run app.py
def home_screen():
    #st.header('home screen')
    style_base_layout()
    header_home()
    style_background_home()
    col1, col2 = st.columns(2, gap= "large")


    with col1:
        st.header("I'm a Teacher")
        st.image("https://i.ibb.co/844D9Lrt/mascot-teacher.png",width=120)
        if st.button('Teacher Portal'):
            st.session_state['login_type']= 'teacher'
            st.rerun()

    with col2:
        st.header("I'm a Student")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png",width=120)
        if st.button('Student Portal'):
            st.session_state['login_type']= 'student'
            st.rerun()

