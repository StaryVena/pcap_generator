#!/bin/bash

docker build -t udfb/http-generator ../../src/http_client/
docker push udfb/http-generator