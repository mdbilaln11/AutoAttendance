# Database Schema

Core tables:

- `users`: authenticated users with role-based permissions.
- `students`: college identity and class placement metadata.
- `face_embeddings`: binary face vectors by student, pose, and quality score.
- `attendance_records`: subject/date attendance facts with recognition confidence.
- `audit_logs`: immutable security and administrative activity records.
