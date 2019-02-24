FROM python:2.7-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN mkdir /app

WORKDIR /app

RUN git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev

WORKDIR /app/ sqlmap-dev
