# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY src/ src/
COPY tests/ tests/
COPY setup.py .

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app/src

# Specify the default command to run your application
CMD ["python", "src/main.py"]
