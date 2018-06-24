# pcap generator
Generation of pcap files using python and docker.


install docker

install docker compose

docker tag mylocalimage:latest username/reponame:tag

docker push username/reponame:tag


docker stack deploy --compose-file docker-compose.yml webservice

docker stack ps webservice

docker stack rm webservice





docker tag udfb:nginx-tcpdump udfb/nginx-tcpdump:init
docker push udfb/nginx-tcpdump:init

"Err": "starting container failed: OCI runtime create failed: container_linux.go:348: starting container process caused \"exec: \\\"/bin/bash\\\": stat /bin/bash: no such file or directory\": unknown",
