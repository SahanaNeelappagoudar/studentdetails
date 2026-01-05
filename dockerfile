FROM python:3.12-slim

WORKDIR /docker_studentdetails

COPY docker_studentdetails.py .

CMD ["python", "docker_studentdetails.py"]