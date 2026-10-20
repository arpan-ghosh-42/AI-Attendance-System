import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image, ImageOps
import numpy as np
from src.pipelines.face_pipeline import predict_attendance, get_enrollment_embedding, train_classifier, distance_to_student, SAME_PERSON_FOR_NEW_SAMPLE
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject, add_face_sample
import time

from src.components.dialog_enroll import enroll_dialog
from src.components.dialog_auto_enroll import auto_enroll_dialog
from src.components.subject_card import subject_card

# navigation callbacks: run before the rerun, so one click = one script run
def _go_home():
    st.session_state['login_type'] = None

def _logout():
    st.session_state['is_logged_in'] = False
    st.session_state.pop('student_data', None)


def _toggle_sample_camera():
    st.session_state.sample_camera_on = not st.session_state.get('sample_camera_on', False)


def improve_face_recognition(student_id):
    camera_on = st.session_state.get('sample_camera_on', False)
    with st.expander("Improve face recognition", icon=":material/face_retouching_natural:", expanded=camera_on):
        st.caption("Add 2-3 more photos (different lighting / angle, face clearly visible). "
                   "More samples make attendance detection much more reliable.")
        st.button("Close camera" if camera_on else "Add a face photo", key="sample_camera_btn",
                  type='primary', icon=':material/photo_camera:', on_click=_toggle_sample_camera)
        if not camera_on:
            return  # the camera element isn't created, so the browser camera stays off

        photo = st.camera_input("Add a face sample", key="extra_face_sample")
        if photo and st.session_state.get("last_face_sample") != photo.file_id:
            st.session_state.last_face_sample = photo.file_id
            with st.spinner("Checking photo..."):
                img = np.array(ImageOps.exif_transpose(Image.open(photo)).convert('RGB'))
                encodings = get_enrollment_embedding(img)
                if len(encodings) != 1:
                    st.warning("Make sure exactly one face is clearly visible.")
                    return
                dist = distance_to_student(encodings[0], student_id)
                if dist is not None and dist > SAME_PERSON_FOR_NEW_SAMPLE:
                    st.error("This doesn't look like the same person as your profile, so it wasn't saved.")
                    return
                count = add_face_sample(student_id, encodings[0].tolist())
                train_classifier()
            st.success(f"Saved! You now have {count} face sample(s). Take another or close the camera.")


def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    join_code = st.query_params.get('join-code')
    if join_code:
        auto_enroll_dialog(join_code)
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"""Welcome, {student_data['name']} """)
        st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace", on_click=_logout)


    st.space()

    improve_face_recognition(student_id)

    c1, c2 =st.columns(2)
    with c1:
        st.header('Your Enrolled Subjects')
    with c2:
        if st.button('Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()


    st.divider()


    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total":0, "attended": 0}

        stats_map[sid]['total'] +=1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1


    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']


        stats = stats_map.get(sid,{"total":0, "attended": 0} )
        attendance_pct = round(stats['attended'] / stats['total'] * 100, 1) if stats['total'] else 0
        def unenroll_button():
                if st.button("Unenroll from this course", type='tertiary', width='stretch', icon=':material/delete_forever:'):
                    unenroll_student_to_subject(student_id, sid)
                    st.toast(f'Unenrolled from {sub["name"]} successfully!')
                    st.rerun()

        with cols[i % 2]:

            subject_card(
                name = sub['name'],
                code =sub['subject_code'],
                section = sub['section'],
                stats = [
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                    ('📊', 'Attendance', f'{attendance_pct}%'),
                ],
                footer_callback=unenroll_button
            )
    footer_dashboard()


def student_screen():


    style_background_dashboard()
    style_base_layout()


    if "student_data" in st.session_state:
        student_dashboard()
        return
    
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.button("Home Screen", type='secondary', key='loginbackbtn', shortcut="control+backspace", on_click=_go_home)

    st.header('Login using FaceID', text_alignment='center')
    st.space()
    st.space()
    
    show_registration = False
    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        img = np.array(ImageOps.exif_transpose(Image.open(photo_source)).convert('RGB'))

        with st.spinner('AI is scanning..'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('Face not found!')
            elif num_faces >1:
                st.warning('Multiple faces found')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id']==student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f'Welcome Back {student["name"]}')
                        st.rerun()
                else:
                    st.info('Face not recognized! You might be a new student!')
                    show_registration = True
    if show_registration:
        with st.container(border=True):
            st.header('Register new Profile')
            new_name = st.text_input("Enter your name", placeholder='E.g. Arpan Ghosh')

            st.subheader('Optional : Voice Enrollment')
            st.info("Enroll your for voice only attendance")


            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like I am present, My name is Akash.')
            except Exception:
                st.error('Audio Data failed!')

            if st.button('Create Account', type='primary'):
                if new_name:
                    with st.spinner('Creating profile..'):
                        img = np.array(ImageOps.exif_transpose(Image.open(photo_source)).convert('RGB'))
                        encodings= get_enrollment_embedding(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Hi {new_name}!')
                                st.rerun()
                        else:
                            st.error('Couldnt capture your facial features for registration')

                else:
                    st.warning('Please enter your name!')


        
    footer_dashboard()