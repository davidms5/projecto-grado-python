# Backend service
FROM python:3.11-slim-buster AS backend
WORKDIR /app/backend
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend .
CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]

# Frontend service
FROM node:16-alpine AS frontend
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend .
CMD ["npm", "start"]

