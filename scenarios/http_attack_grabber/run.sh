#!/bin/bash

docker stack deploy --compose-file docker-compose.yml webservice
# wait 10 minutes
for a in $( seq 10)
do sleep 60
echo $a
done
#print running services
docker stack ps  --no-trunc webservice
#kill running webservice
docker stack rm webservice