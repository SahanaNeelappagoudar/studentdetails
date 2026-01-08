FROM python:3.14.0
WORKDIR /studentdetails
COPY . .
RUN pip install --no-cache-dir pytest
# Run tests at build time (CI)
CMD pytest -v --cache-clear && python studentdetails.py