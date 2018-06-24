#!/bin/bash

docker build -t udfb/nginx-tcpdump src/nginx/
docker push udfb/nginx-tcpdump
docker stack deploy --compose-file docker-compose01.yml webservice
sleep 120
docker stack ps webservice
#docker service logs webservice_http_crawler
#docker service logs webservice_web-nginx
docker stack rm webservice