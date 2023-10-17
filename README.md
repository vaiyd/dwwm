# Python

Link :
* https://www.python.org/downloads/release/python-31012/
* https://bootstrap.pypa.io/get-pip.py
* https://www.sqlalchemy.org/
* https://flask.palletsprojects.com/en/2.3.x/
* https://flask-restful.readthedocs.io/en/latest/

```bash
#Se déplacer à la racine du projet
python get-pip.py
pip install -r requirements.txt
```


# Docker

## Installation

Link :
* https://docs.docker.com/engine/install/debian/
* https://docs.docker.com/engine/install/linux-postinstall/

Prerequisite : go to https://docs.docker.com/engine/install/debian/#install-using-the-repository to create a Debian repotository to permit installation of Docker.

```bash  
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo adduser --system docker
sudo newgrp docker 
sudo usermod -g docker docker
docker run hello-world
```

## Docker Managaging Tool (Portainer)

Installation of portainer with docker and create volume to save portainer custom configuration. 

```bash
docker volume create portainer_data
docker run -d --name epsi-portainer --restart=always -p 8000:8000 -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```

[OPTIONNEL], only to connect external docker to you're portainer
```bash
sudo vi /lib/systemd/system/docker.service
```
You need to find "ExecStart" and add "-H" parameters to permit portainer connection if portainer is installed on another Docker
```ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375 --containerd=/run/containerd/containerd.sock```
```bash
sudo systemctl daemon-reload
sudo service docker restart
# To Verify
curl http://localhost:2375/images/json
```
Go to portainer (https://localhost:9000)
Environnements -> Add new -> Docker -> Start Wizard
Choose Api, configuration exemple  :
* Name = docker-epsi
* URL = 192.168.X.X:2375
