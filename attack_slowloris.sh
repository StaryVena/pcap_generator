#!/bin/bash

# docker build -t udfb/slowloris src/attack_slowloris/
# docker push udfb/slowloris
docker stack deploy --compose-file docker-compose-slowloris.yml webservice
for a in $( seq 10)
do sleep 60
echo $a
done
docker stack ps webservice
docker stack rm webservice