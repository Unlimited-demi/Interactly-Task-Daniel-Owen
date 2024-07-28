# Use an official Python runtime as a parent image
FROM python:3.9-slim AS backend

# Set the working directory in the container for the backend
WORKDIR /app/backend

# Copy the backend directory into the container
COPY backend/ ./

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the backend runs on
EXPOSE 5000

# Use a new stage to build the frontend
FROM node:16 AS frontend

# Set the working directory in the container for the frontend
WORKDIR /app/frontend

# Copy package.json and package-lock.json first
COPY frontend/package*.json ./

# Install frontend dependencies
RUN npm install

# Copy the rest of the frontend files
COPY frontend/ ./

# Build the frontend
RUN npm run build

# Final stage
FROM python:3.9-slim

# Set the working directory in the final container
WORKDIR /app

# Copy the backend files from the previous stage
COPY --from=backend /app/backend /app/backend

# Copy the built frontend files from the previous stage
COPY --from=frontend /app/frontend/build /app/frontend/build

# Expose the ports the app runs on
EXPOSE 5000 80

# Set environment variables (if any)
ENV FLASK_APP=/app/backend/app.py

# Define the command to run the app
CMD ["flask", "run", "--host=0.0.0.0"]
