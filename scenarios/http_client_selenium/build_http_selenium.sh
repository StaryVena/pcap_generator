#!/bin/bash

docker build -t udfb/http-selenium ../../src/http_selenium_script/
docker push udfb/http-selenium