FROM python:3.9-slim-buster

# ENV MY_VAR=my_value

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
