FROM python:3.11.9-slim

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y python3-dev gcc libc-dev libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./django/requirements.txt /app/backend/
RUN pip install -r backend/requirements.txt

# Add necessary files
ADD ./django /app/backend
ADD ./docker /app/docker
ADD ./django/.env.local /app/backend/

# Set permissions for the entrypoint script
RUN chmod +x /app/docker/backend/wsgi-entrypoint.sh