FROM python:3.7-alpine

RUN mkdir /app

COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

COPY smb_client.py .
COPY crawler_client.py .
COPY secret_files.txt .