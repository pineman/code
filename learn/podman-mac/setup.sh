#!/bin/sh
brew install podman vagrant
#vagrant plugin install vagrant-parallels
vagrant up
podman system connection add arch --identity ~/.ssh/id_ecdsa ssh://vagrant@10.13.37.2/run/user/1000/podman/podman.sock
podman system connection default arch
podman info
podman run -it docker.io/ubuntu:20.04
