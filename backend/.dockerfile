# Dockerfile for Django app

# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the app code to the working directory
COPY . .

# Expose port 8000
EXPOSE 8000

# Start the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
