# AutoAttendance Web Test App for Windows

This static web app is intended for quick end-to-end testing from a Windows laptop using Chrome or Microsoft Edge. It does not replace the Flutter app; it gives teachers/developers a browser workflow for uploading or recording a short classroom video and sending it to the FastAPI preview endpoint.

## Prerequisites

- Windows 10/11
- Chrome or Microsoft Edge
- Python 3.12+
- The backend running at `http://localhost:8000`

## Start the backend

From the repository root:

```powershell
copy backend\.env.example backend\.env
docker compose up --build
```

If you are not using Docker, run the FastAPI app from `backend/` after installing `requirements.txt`.

## Start the web tester

From the repository root:

```powershell
cd web-test-app
py -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

## Test workflow

1. Confirm the API status pill says `API online`.
2. Enter the department, year, section, and subject.
3. Upload a classroom video or click **Start Camera** and **Record 10s**.
4. Click **Send Preview**.
5. Review raw JSON plus grouped present, absent, and unknown/rejected candidates.

Camera access requires `localhost` or HTTPS in modern browsers.
