FROM python:3.12-slim
WORKDIR /docker_studentdetails
COPY . .
CMD ["python","docker_studentdetails.py"]