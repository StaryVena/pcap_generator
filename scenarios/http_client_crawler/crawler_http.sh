#!/bin/bash

docker stack deploy --compose-file docker-compose-http-client.yml webservice
sleep 30
#docker stack ps --no-trunc webservice
docker stack rm webservice