#!/bin/bash

docker build -t udfb/lighttpd-tcpdump src/lighttpd/
docker push udfb/lighttpd-tcpdump
docker stack deploy --compose-file docker-compose-lighttpd-slowloris.yml webservice
for a in $( seq 10)
do sleep 60
echo $a
done
docker stack ps  --no-trunc webservice
docker stack rm webservice