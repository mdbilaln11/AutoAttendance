# Deployment Guide

1. Replace `SECRET_KEY` and database credentials with managed secrets.
2. Run PostgreSQL with automated backups and encryption at rest.
3. Deploy FastAPI behind HTTPS ingress and a WAF.
4. Attach GPU-capable workers for InsightFace processing at scale.
5. Store videos and face crops in private object storage with short retention.
6. Enable logs, metrics, tracing, and audit-log retention policies.
