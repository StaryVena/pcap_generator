#!/bin/bash

docker build -t udfb/ihulk src/attack_http_ihulk/
docker push udfb/ihulk

docker stack deploy --compose-file docker-compose-ihulk.yml webservice
sleep 600
docker stack ps --no-trunc webservice
docker stack rm webservice