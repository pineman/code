#!/bin/bash
set -euxo pipefail
curl -O https://releases.hashicorp.com/nomad/1.0.4/nomad_1.0.4_linux_amd64.zip
unzip nomad_1.0.4_linux_amd64.zip
curl -O https://releases.hashicorp.com/nomad-driver-podman/0.2.0/nomad-driver-podman_0.2.0_linux_amd64.zip
unzip nomad-driver-podman_0.2.0_linux_amd64.zip
sudo vagrant up
sudo cp /var/lib/libvirt/images/proxmox-nomad-cluster_default.img .
sudo chown $USER: ./*
qemu-img rebase -b '' proxmox-nomad-cluster_default.img
for i in {5..7}; do
  scp proxmox-nomad-cluster_default.img root@192.168.1.$i:
  ssh root@192.168.1.$i qm create 60$i
  ssh root@192.168.1.$i qm importdisk 60$i proxmox-nomad-cluster_default.img local-lvm
done
# execute manual steps:
# 1. change properties on web ui: add network and disk
# 1. sudo sed -i 's/n1/n$i/g' /etc/hostname
# 1. sudo sed -i 's/192.168.1.10/192.168.1.1$i/g' /etc/systemd/network/eth0.network
# 1. sudo reboot
# 1. nomad server join 192.168.1.10
# 1. nomad node config -update-servers 192.168.1.10:4647
# OR use consul https://learn.hashicorp.com/tutorials/nomad/clustering
