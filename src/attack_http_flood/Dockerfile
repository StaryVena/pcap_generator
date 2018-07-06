FROM python:alpine

RUN pip install --no-cache-dir --upgrade requests netaddr

COPY wreckuests /usr/src/app

WORKDIR /usr/src/app

# CMD [ "python", "wreckuests.py", "-v", "https://www.example.com", "-t", "2"]