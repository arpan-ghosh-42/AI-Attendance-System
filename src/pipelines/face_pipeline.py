import dlib
import numpy as np
import face_recognition_models
import streamlit as st

from src.database.db import get_all_students, face_samples


# Open-set face matching tuned for accuracy (false "present" is worse than a miss).
# dlib's usual 0.6 cut-off comes from LFW and is far too loose for many faces
# (notably women and South Asian faces), so we match much more strictly.
MATCH_THRESHOLD = 0.48   # max embedding distance to accept a match
AMBIGUITY_MARGIN = 0.06  # best match must beat the runner-up student by this much
MAX_SIDE = 1600          # downscale huge photos (speed; HOG works fine at this size)
MIN_SIDE_FOR_UPSAMPLE = 1200  # small/low-res photos get an extra upsample pass


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


def _prepare_image(image_np):
    """uint8 RGB, at most MAX_SIDE px on the long side."""
    img = np.asarray(image_np)
    if img.ndim == 2:
        img = np.stack([img] * 3, axis=-1)
    elif img.shape[2] == 4:
        img = img[:, :, :3]
    if img.dtype != np.uint8:
        img = img.astype(np.uint8)

    h, w = img.shape[:2]
    if max(h, w) > MAX_SIDE:
        from PIL import Image
        scale = MAX_SIDE / max(h, w)
        img = np.asarray(Image.fromarray(img).resize((int(w * scale), int(h * scale)), Image.LANCZOS))
    return np.ascontiguousarray(img)


def _detect(detector, img, thorough=True):
    if not thorough:
        # selfie / login photo: one large face, normal resolution is enough (much faster)
        faces = detector(img, 0)
        return faces if len(faces) else detector(img, 1)

    faces = detector(img, 1)
    # small faces in a group photo / low-res webcam frame: look harder
    if len(faces) == 0 or max(img.shape[:2]) < MIN_SIDE_FOR_UPSAMPLE:
        more = detector(img, 2)
        if len(more) > len(faces):
            faces = more
    return faces


def get_face_embeddings(image_np, num_jitters=1, thorough=True):
    detector, sp, facerec = load_dlib_models()
    img = _prepare_image(image_np)
    faces = _detect(detector, img, thorough)

    encodings = []
    for face in faces:
        shape = sp(img, face)
        face_descriptor = facerec.compute_face_descriptor(img, shape, num_jitters)  # 128-d embedding
        encodings.append(np.array(face_descriptor))
    return encodings


def get_enrollment_embedding(image_np):
    """Embedding used when registering a student: averaged over 10 jittered
    crops, which is noticeably more stable than a single pass."""
    encodings = get_face_embeddings(image_np, num_jitters=10, thorough=False)
    return encodings


@st.cache_resource(ttl=300)
def get_trained_model():
    student_db = get_all_students()
    if not student_db:
        return None

    ids, embeddings = [], []
    for student in student_db:
        for embedding in face_samples(student.get('face_embedding')):
            ids.append(int(student['student_id']))
            embeddings.append(np.array(embedding, dtype=np.float64))

    if not embeddings:
        return None

    return {'ids': ids, 'X': np.vstack(embeddings)}


def train_classifier():
    # only drop the enrolled-faces cache, not the dlib models
    get_trained_model.clear()
    return bool(get_trained_model())


def _match(encoding, model_data):
    """Return (student_id, distance) for a confident match, else (None, distance)."""
    dists = np.linalg.norm(model_data['X'] - encoding, axis=1)
    ids = model_data['ids']

    # best distance per student (a student may have several stored embeddings)
    per_student = {}
    for sid, d in zip(ids, dists):
        if d < per_student.get(sid, np.inf):
            per_student[sid] = d
    ranked = sorted(per_student.items(), key=lambda kv: kv[1])

    best_id, best = ranked[0]
    if best > MATCH_THRESHOLD:
        return None, best
    if len(ranked) > 1 and ranked[1][1] - best < AMBIGUITY_MARGIN:
        return None, best  # too close to call between two students
    return best_id, best


SAME_PERSON_FOR_NEW_SAMPLE = 0.55  # a new sample must resemble the student's existing ones


def distance_to_student(encoding, student_id):
    model_data = get_trained_model()
    if not model_data:
        return None
    mask = np.array(model_data['ids']) == int(student_id)
    if not mask.any():
        return None
    return float(np.min(np.linalg.norm(model_data['X'][mask] - encoding, axis=1)))


def predict_attendance(class_image_np, thorough=True):
    encodings = get_face_embeddings(class_image_np, thorough=thorough)

    detected_student = {}
    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)

    # each student can be matched by at most one face (keep the closest)
    best_for_student = {}
    for encoding in encodings:
        sid, dist = _match(encoding, model_data)
        if sid is not None and dist < best_for_student.get(sid, np.inf):
            best_for_student[sid] = dist

    for sid in best_for_student:
        detected_student[sid] = True

    all_students = sorted(set(model_data['ids']))
    return detected_student, all_students, len(encodings)
