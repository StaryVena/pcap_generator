# PCAP generator
Generation of pcap files using python and docker.

## Installation
Docker, docker compose and docker swarm is needed to run scenarios.

1. Install Docker on Linux: 
[CentOS](https://docs.docker.com/install/linux/docker-ce/centos/), 
[Debian](https://docs.docker.com/install/linux/docker-ce/debian/),
[Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/), or
[Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/).

2. Post installation steps do run Docker as non sudo user:
https://docs.docker.com/install/linux/linux-postinstall/

3. Install [Docker Compose](https://docs.docker.com/compose/install/).

4. *Optional* for Docker Swarm on multiple computers -
[init cluster](https://docs.docker.com/engine/swarm/swarm-tutorial/).

## Project structure
There are several folder in the project, below is a description of each.

###### `output` directory
Here are stored outputs from container like tcpdump, http crawler logs,
selenium tests ouptput, etc. Use the directory for any files needed to be
generated from containers. Include .gitignore file to write directory to
git repository (but not content).

###### `runs` directory
Contains settings for sambla clients and server. This directory will be
deleted in next release, do not use this directory.

###### `scenarios` directory
Here is the complete list of all implemented scenarios. In each subdirectory
is usually included documentation (README.md) file, bash script for running
scenario and docker-compose.yml file.

###### `sides` directory
This directory contains test files for Selenium IDE. Also this directory
will be moved to src directory in the future.

###### `src` directory
To this directory belongs all source codes for containers. All containers
have its own subdirectory.

###### `support` directory
Directory for another files which are not relevant for running containers.
Put here web pages, images, or any other files.


###### Other files in the root directory

`generate_pdf.sh` is a bash script which generates `manual.pdf` file from
this file and README.md in `scenarios` subdirectories. It uses Pandoc
 which is a universal document converter. `pcap_template.latex` is latex template for the
 output pdf.

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
Create new tag (default is latest):

```bash
docker tag mylocalimage:latest username/reponame:tag
```

Example:

```bash
docker tag udfb:nginx-tcpdump udfb/nginx-tcpdump
```

Add new version to the Docker Hub:

```bash
docker push username/reponame:tag
```

Example:

```bash
docker push udfb/nginx-tcpdump
```


Shows log for given service:

```bash
docker service logs webservice_http_fuzz
```


#### Generate pdf version of this file:

https://www.markdowntopdf.com/

or [directly](http://gitprint.com/) from [github](https://gitprint.com/StaryVena/pcap_generator/blob/master/README.md),

or just install [Pandoc](https://pandoc.org/) and run generate_pdf.sh to
generate whole documentation:
```bash
bash generate_pdf.sh
```
