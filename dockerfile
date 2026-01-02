FROM python:3.14.0 
WORKDIR /studentdetails
COPY . .
CMD ["python","studentdetails.py"]