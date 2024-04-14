# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Set an environment variable to indicate that we are running inside Docker
ENV RUNNING_IN_DOCKER=true

# Run the tests
RUN python -m pytest -v -s

CMD tail -f /dev/null
