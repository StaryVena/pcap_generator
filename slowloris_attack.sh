#!/bin/bash

docker build -t udfb/slowloris src/attack_slowloris/
docker push udfb/slowloris
docker stack deploy --compose-file docker-compose-slowloris.yml webservice
sleep 600
docker stack ps webservice
docker stack rm webservice