# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy local files to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask API port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
