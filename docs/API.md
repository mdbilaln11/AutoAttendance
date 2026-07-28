# API Documentation

Base path: `/api/v1`.

## Attendance

`POST /attendance/preview` accepts multipart form fields `department`, `year`, `section`, `subject`, and `video`. It returns recognized present candidates, absent student IDs, unknown faces, and confidence values for teacher verification.

## Health

`GET /health` returns service status for readiness probes.
