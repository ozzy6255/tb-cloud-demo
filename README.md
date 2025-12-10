# TB Cloud Demo

Legacy system migration and modernization project.

## Architecture
- **Backend**: Python FastAPI + SQLite (Port 8002)
- **Frontend**: Vue 3 + Vite (Port 5173)

## Quick Start (Local)

### 1. Backend
```bash
cd src/backend
# python3 -m venv venv (if not created)
# source ../../venv/bin/activate
pip install -r requirements.txt
export DB_TYPE=sqlite
uvicorn main:app --port 8002 --reload
```

### 2. Frontend
```bash
cd src/frontend_vite
npm install
npm run dev
```

## Deployment
Push to GitHub to trigger Render deployment.
