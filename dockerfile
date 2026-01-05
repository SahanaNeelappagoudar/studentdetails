FROM python:3.14.0
WORKDIR /docker_studentdetails
COPY . .
CMD ["python","docker_studentdetails.py"]