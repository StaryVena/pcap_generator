#!/bin/bash

docker build -t udfb/apache-tcpdump src/apache/
docker push udfb/apache-tcpdump