# Use official Python runtime as base image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY main.py .
COPY tests/ tests/

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run tests by default (can be overridden)
CMD ["python", "main.py"]
