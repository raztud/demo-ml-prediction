# Use Python image as base
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy Python script into the container
COPY downloader.py .

# Set the entry point to the Python script
ENTRYPOINT ["python", "downloader.py"]
