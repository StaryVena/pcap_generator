#!/bin/bash

docker build -t udfb/nginx-tcpdump ../../src/nginx/
docker push udfb/nginx-tcpdump