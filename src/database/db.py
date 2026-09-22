from src.database.config import supabase
import bcrypt


def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())

def check_teacher_exists(username):
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0

def create_teacher(username, password, name):
    data = {"username": username, "password": hash_pass(password), "name": name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher["password"]):
            return teacher
    return None

def create_subject(subject_code, name, section, teacher_id):
    data = {"subject_code": subject_code, "name": name, "section": section, "teacher_id": teacher_id}
    response = supabase.table("subjects").insert(data).execute()
    return response.data

def get_teacher_subjects(teacher_id):
    response = supabase.table("subjects").select("*").eq("teacher_id", teacher_id).execute()
    subjects = response.data

    for subject in subjects:
        sid = subject["subject_id"]

        students_res = supabase.table("subject_students").select("student_id", count="exact").eq("subject_id", sid).execute()
        subject["total_students"] = students_res.count or 0

        classes_res = supabase.table("attendance_logs").select("timestamp").eq("subject_id", sid).execute()
        subject["total_classes"] = len({row["timestamp"] for row in classes_res.data})

    return subjects

def get_attendance_for_teacher(teacher_id):
    subjects_res = supabase.table("subjects").select("subject_id").eq("teacher_id", teacher_id).execute()
    subject_ids = [s["subject_id"] for s in subjects_res.data]

    if not subject_ids:
        return []

    response = (
        supabase.table("attendance_logs")
        .select("*, subjects(*)")
        .in_("subject_id", subject_ids)
        .order("timestamp", desc=True)
        .execute()
    )
    return response.data

def create_attendance(logs):
    response = supabase.table("attendance_logs").insert(logs).execute()
    return response.data

def get_subject_attendance_details(subject_id):
    enrolled_res = supabase.table("subject_students").select("*, students(*)").eq("subject_id", subject_id).execute()
    enrolled_students = enrolled_res.data

    logs_res = supabase.table("attendance_logs").select("*").eq("subject_id", subject_id).execute()
    logs = logs_res.data

    total_classes = len({log["timestamp"] for log in logs})

    student_stats = []
    for node in enrolled_students:
        student = node["students"]
        sid = student["student_id"]
        student_logs = [log for log in logs if log["student_id"] == sid]
        classes_for_student = len(student_logs)
        attended = sum(1 for log in student_logs if log.get("is_present"))
        skipped = classes_for_student - attended
        percentage = (attended / classes_for_student * 100) if classes_for_student else 0

        student_stats.append({
            "name": student["name"],
            "attended": attended,
            "skipped": skipped,
            "total_classes": classes_for_student,
            "percentage": round(percentage, 1),
        })

    return {
        "total_students": len(enrolled_students),
        "total_classes": total_classes,
        "students": student_stats,
    }

def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data

def create_student(name, face_embedding=None, voice_embedding=None):
    data = {"name": name, "face_embedding": face_embedding, "voice_embedding": voice_embedding}
    response = supabase.table("students").insert(data).execute()
    return response.data

def get_student_subjects(student_id):
    response = supabase.table("subject_students").select("*, subjects(*)").eq("student_id", student_id).execute()
    return response.data

def get_student_attendance(student_id):
    response = supabase.table("attendance_logs").select("*").eq("student_id", student_id).execute()
    return response.data

def enroll_student_to_subject(student_id, subject_id):
    data = {"student_id": student_id, "subject_id": subject_id}
    response = supabase.table("subject_students").insert(data).execute()
    return response.data

def unenroll_student_to_subject(student_id, subject_id):
    response = (
        supabase.table("subject_students")
        .delete()
        .eq("student_id", student_id)
        .eq("subject_id", subject_id)
        .execute()
    )
    return response.data
