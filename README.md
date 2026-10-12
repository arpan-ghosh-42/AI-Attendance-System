# SnapClass — AI Attendance System

<p align="center">
  <img src="assets/images/logo.webp" alt="SnapClass logo" width="150" />
</p>

<p align="center">
  A Streamlit-based attendance platform that helps teachers record attendance from classroom photos or voice recordings, while giving students a simple biometric sign-in and attendance dashboard.
</p>

## What it does

SnapClass supports two roles:

- **Teachers** can create subjects, share enrollment links or QR codes, record attendance from uploaded/captured classroom photos or audio, review results before saving, and explore attendance records.
- **Students** can register a profile with a face embedding and optional voice embedding, sign in with Face ID, join subjects with a code or shared link, and see attendance for each subject.

## Highlights

- Face-based attendance using dlib face embeddings and an SVM classifier
- Voice-based attendance using Resemblyzer speaker embeddings
- Teacher and student portals with separate onboarding flows
- Subject creation, enrollment, QR/link sharing, and unenrollment
- Attendance review before records are saved
- Per-subject attendance metrics and teacher-facing attendance reports
- Supabase persistence with password hashing via bcrypt
- Responsive dark UI built with Streamlit

## Tech stack

| Area | Tools |
| --- | --- |
| Frontend | Streamlit |
| Database | Supabase |
| Face recognition | dlib, `face_recognition_models`, scikit-learn |
| Voice recognition | Resemblyzer, librosa |
| Data and media | NumPy, pandas, Pillow, Segno |

## Getting started

### Prerequisites

- Python **3.11**
- A Supabase project
- A camera and microphone for the live capture flows (optional for photo/audio upload)

### 1. Clone and create a virtual environment

```powershell
git clone https://github.com/arpan-ghosh-42/Ai-Attendance-System.git
cd Ai-Attendance-System
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On macOS or Linux, activate the environment with:

```bash
source venv/bin/activate
```

### 2. Configure Supabase

Create `.streamlit/secrets.toml` locally. This file is intentionally ignored by Git.

```toml
supabase_url = "https://your-project.supabase.co"
supabase_key = "your-supabase-anon-key"
```

The app expects these tables in Supabase:

| Table | Purpose |
| --- | --- |
| `teachers` | Teacher profiles and hashed passwords |
| `students` | Student profiles plus face and optional voice embeddings |
| `subjects` | Subjects created by teachers |
| `subject_students` | Student-to-subject enrollment records |
| `attendance_logs` | Attendance outcomes for each subject session |

Use appropriately restrictive Supabase Row Level Security policies before deploying the app. Biometric embeddings are sensitive personal data and should only be stored with informed consent.

### 3. Run the app

```powershell
streamlit run app.py
```

Then open the local URL printed by Streamlit, usually `http://localhost:8501`.

## How attendance works

1. Students create a profile from a face capture and may add a voice sample.
2. Teachers create a subject and share its join code, link, or QR code.
3. Students enroll in the subject.
4. For a class session, the teacher either supplies classroom photos or records classroom audio.
5. SnapClass matches the captured embeddings against enrolled student profiles, presents results for review, and saves confirmed attendance to Supabase.

Face matching uses a 128-dimensional dlib embedding with an SVM classifier and a distance threshold. Voice matching compares Resemblyzer embeddings using cosine similarity. These signals can be affected by recording conditions, image quality, and the number of enrolled profiles, so teachers should always review results before saving them.

## Project structure

```text
.
├── app.py                     # Streamlit entry point and portal routing
├── assets/images/             # Branding and interface assets
├── src/
│   ├── components/            # Reusable cards, headers, dialogs, and flows
│   ├── database/              # Supabase client configuration and data access
│   ├── pipelines/             # Face and voice recognition pipelines
│   ├── screens/               # Home, teacher, and student screens
│   └── ui/                    # App layout, theme styling, and assets helpers
├── .streamlit/config.toml     # Streamlit theme configuration
└── requirements.txt           # Python dependencies
```

## Privacy and responsible use

SnapClass processes biometric identifiers. Get explicit consent before enrolling anyone, restrict access to the Supabase project, apply least-privilege database policies, and provide a clear process for profile deletion. This project is intended to assist attendance-taking—not replace teacher judgment or institutional privacy requirements.

## Contributing

Issues and pull requests are welcome. Please avoid committing `.streamlit/secrets.toml`, `.env` files, student records, or biometric embeddings.
