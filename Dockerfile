# Stage 1: Build Vue Frontend
FROM node:18-alpine AS frontend-builder
WORKDIR /app/frontend
COPY src/frontend_vite/package*.json ./
RUN npm install
COPY src/frontend_vite/ ./
RUN npm run build
RUN echo "=== Build completed, checking dist/ ===" && ls -la dist/ || echo "dist/ not found!"

# Stage 2: Python Backend + Serve Frontend
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

# Copy built frontend from stage 1
COPY --from=frontend-builder /app/frontend/dist /app/static
RUN echo "=== Checking /app/static/ ===" && ls -la /app/static/ || echo "/app/static/ is empty or missing!"

# Set environment
ENV DB_TYPE=sqlite
ENV PORT=8000

EXPOSE 8000

# Run backend
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
