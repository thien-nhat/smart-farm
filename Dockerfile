# Use an official Python runtime as a parent image
FROM python:3.8.18-bookworm

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install tensorrt
# Make port 5000 available to the world outside this container
EXPOSE 5001

# Run main.py when the container launches
# CMD ["python", "main.py"]
CMD exec gunicorn --bind :5001 --workers 1 --threads 8 main:app
