FROM python:13.14.0 
WORKDIR /studentdetails
COPY . .
RUN pip install pytest
CMD ["pytest","-v"]