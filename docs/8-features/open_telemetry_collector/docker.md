# Install Docker Desktop on Ubuntu

## Prerequisites

sudo apt install gnome-terminal

## Install Docker Desktop

sudo apt-get update
sudo apt install ./docker-desktop-amd64.deb

## Enable / Launch / Stop Docker Desktop

systemctl --user enable docker-desktop
systemctl --user start docker-desktop
systemctl --user stop docker-desktop

## Upgrade Docker Desktop

sudo apt install ./docker-desktop-amd64.deb

## Verify

docker compose version
docker --version
docker version

##

docker run -d -p 80:80 docker/getting-started

```
# Set up Docker's package repository. See step one of Install using the apt repository.
## Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

## Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
```
