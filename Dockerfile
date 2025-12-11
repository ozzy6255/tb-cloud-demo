# Simplified Dockerfile - Frontend pre-built locally
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    gcc \
    g++ \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install
COPY src/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY src/backend/ .

# Copy pre-built frontend (built locally before git push)
COPY src/frontend_vite/dist /app/static

# Verify static files exist
RUN ls -la /app/static/ && echo "Static files verified!"

# Set environment
ENV DB_TYPE=sqlite
ENV PORT=8000

EXPOSE 8000

# Run backend
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
