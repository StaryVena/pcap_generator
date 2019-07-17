# PCAP generator
Generation of pcap files using python and docker.

## Installation
Docker, docker compose and docker swarm is needed to run scenarios.

1. Install Docker on Linux: 
[CentOS](https://docs.docker.com/install/linux/docker-ce/centos/), 
[Debian](https://docs.docker.com/install/linux/docker-ce/debian/),
[Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/), or
[Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/).

2. Post installation steps do run Docker as non sudo user: https://docs.docker.com/install/linux/linux-postinstall/

3. Install [Docker Compose](https://docs.docker.com/compose/install/).

4. *Optional* for Docker Swarm on multiple computers - [init cluster](https://docs.docker.com/engine/swarm/swarm-tutorial/) 

## Usage

All scenarios are in the `scenarios` directory. 
Scenarios can be run by `cd` to the directory and run bash script `bash run.sh.`
The script runs the docker-compose file, waits 10 minutes and then ps containers and kills them.

Manual way to run a scenario:

```bash
docker stack deploy --compose-file docker-compose.yml webservice

```

Monitor running containers:

```bash
docker stack ps  --no-trunc webservice
```

Show logs for given service:
```bash
docker service logs webservice_[container_name]
```

Terminate running scenario:
```bash
docker stack rm webservice
```

Note: in all scenarios is `webservice` name of service which containers run under.

## Another docker useful commands

```bash
docker tag mylocalimage:latest username/reponame:tag
```

```bash
docker push username/reponame:tag
```

```bash
docker service logs webservice_http_fuzz
```

```bash
docker tag udfb:nginx-tcpdump udfb/nginx-tcpdump
```

```bash
docker push udfb/nginx-tcpdump
```

##### Generate pdf version of this file:

https://www.markdowntopdf.com/

or [directly](http://gitprint.com/) from [github](https://gitprint.com/StaryVena/pcap_generator/blob/master/README.md).

