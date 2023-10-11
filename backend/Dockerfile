# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /backend

EXPOSE 5000:5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container
COPY . .

# Set the entry point to run the Flask application
CMD ["sh", "-c", "sleep 5 && python -m flask run --host=0.0.0.0"]
