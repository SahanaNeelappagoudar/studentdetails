# Use an official Python runtime as a parent image
FROM python:3.13
COPY . .

# Set the working directory in the container
WORKDIR /studentdetails

RUN pip install --no-cache-dir pytest

RUN pytest
# Run the script
ENTRYPOINT  ["python", "studentdetails.py"]