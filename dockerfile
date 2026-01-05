FROM python:3.12-slim
WORKDIR /docker_studentdetails
copy . .
COPY . /app
CMD ["python","docker_studentdetails.py"]