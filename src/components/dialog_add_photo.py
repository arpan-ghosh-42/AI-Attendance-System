import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from PIL import Image, ImageOps
import time


def _open_upright(f):
    # phone photos are often stored sideways with an EXIF rotation flag;
    # the face detector needs them upright
    return ImageOps.exif_transpose(Image.open(f)).convert('RGB')


def _set_photo_tab(tab):
    st.session_state.photo_tab = tab


@st.dialog("Capture or upload photos")
def add_photos_dialog():

    st.write('Add classroom photos to scan for attendance')

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'tertiary'
        st.button('Camera', type=type_camera, width='stretch', on_click=_set_photo_tab, args=('camera',))



    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'tertiary'
        st.button('Upload photos', type=type_upload, width='stretch', on_click=_set_photo_tab, args=('upload',))

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Take Snapshot', key='dialog_cam')
        if cam_photo:
            st.session_state.attendance_images.append(_open_upright(cam_photo))
            st.toast('Photo Captured')
            st.rerun()


    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader( 'choose image files', type=['jpg', 'png', 'jpeg' ], accept_multiple_files=True, key='dialog_upload')

        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(_open_upright(f))
            
            st.toast('Photo Uploaded Successfully')
            st.rerun()

    st.divider()
    if st.button('Done', type='primary', width='stretch'):
        st.rerun()
