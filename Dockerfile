# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
#COPY requirements.txt .

# Install virtualenv
#RUN pip install virtualenv

# Create a virtual environment
#RUN virtualenv venv

# Install any needed packages specified in requirements.txt
#RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

# Run the application
ENTRYPOINT ["streamlit", "run", "code/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
