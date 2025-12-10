FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
# unixodbc-dev & g++ are for pyodbc compatibility (even if we use sqlite)
# curl/gnupg are standard utilities
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    g++ \
    curl \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for cache efficiency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment to use SQLite
ENV DB_TYPE=sqlite

# Expose port (Render automatically maps 80 to this user-defined port usually, but 8000 is standard)
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
