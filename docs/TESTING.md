# Testing Guide

You can test AutoAttendance without using the static website. The options below are useful for Windows developers, backend engineers, QA testers, and mobile developers.

## 1. FastAPI Swagger UI

Start the backend:

```powershell
docker compose up --build
```

Open the built-in API documentation:

```text
http://localhost:8000/docs
```

Use `POST /api/v1/attendance/preview` to upload a video file and submit `department`, `year`, `section`, and `subject` form fields.

## 2. PowerShell API Test

PowerShell can submit a video directly to the API without a browser UI.

```powershell
$Form = @{
  department = 'Computer Science'
  year = '3'
  section = 'A'
  subject = 'Artificial Intelligence'
  video = Get-Item 'C:\path\to\classroom-video.mp4'
}
Invoke-RestMethod -Uri 'http://localhost:8000/api/v1/attendance/preview' -Method Post -Form $Form
```

Health check:

```powershell
Invoke-RestMethod -Uri 'http://localhost:8000/health' -Method Get
```

## 3. curl API Test

Use `curl` from Windows Terminal, Git Bash, macOS, or Linux.

```bash
curl http://localhost:8000/health
```

Submit a classroom video:

```bash
curl -X POST http://localhost:8000/api/v1/attendance/preview \
  -F "department=Computer Science" \
  -F "year=3" \
  -F "section=A" \
  -F "subject=Artificial Intelligence" \
  -F "video=@/path/to/classroom-video.mp4"
```

## 4. Postman or Insomnia

1. Start the backend at `http://localhost:8000`.
2. Create a `POST` request to `http://localhost:8000/api/v1/attendance/preview`.
3. Choose `Body` -> `form-data`.
4. Add text fields: `department`, `year`, `section`, `subject`.
5. Add file field: `video`.
6. Send the request and inspect the JSON response.

## 5. Automated Backend Tests

Install dependencies once:

```powershell
cd backend
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run tests:

```powershell
pytest
```

Run only the AI pipeline tests:

```powershell
pytest tests/test_pipeline.py
```

Run only API tests:

```powershell
pytest tests/test_api.py
```

## 6. Docker Container Smoke Test

Start the stack:

```powershell
docker compose up --build
```

In a second terminal, verify the API:

```powershell
curl http://localhost:8000/health
```

Watch API logs:

```powershell
docker compose logs -f api
```

## 7. Flutter App Testing

Install Flutter dependencies:

```powershell
cd frontend
flutter pub get
```

Run the app in Chrome:

```powershell
flutter run -d chrome
```

Run Flutter static analysis:

```powershell
flutter analyze
```

Run Flutter tests when test files are added:

```powershell
flutter test
```

## 8. AI Pipeline Unit Testing

The current AI pipeline can be tested independently of FastAPI and the database. The pipeline test validates cosine matching, confidence thresholds, liveness gating, and duplicate prevention.

```powershell
cd backend
pytest tests/test_pipeline.py -q
```

## Recommended Testing Order

1. `docker compose up --build`
2. `curl http://localhost:8000/health`
3. `pytest` from `backend/`
4. Swagger UI or curl multipart video upload
5. Windows web tester or Flutter UI for user-flow validation
