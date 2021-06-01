#!/bin/bash
set -x

./clean.sh
sleep 10s

cd k3os
git apply ../mbr.patch

modprobe nbd max_part=10
curl -OL -C - https://github.com/rancher/k3os/releases/download/v0.20.6-k3s1r0/k3os-amd64.iso

qemu-img create -f qcow2 s1.qcow2 20G
qemu-nbd -c /dev/nbd0 s1.qcow2
k3os/install.sh --config s1.yml /dev/nbd0 k3os-amd64.iso
qemu-nbd -d /dev/nbd0
virsh define --file s1.xml
virsh start k3os-s1

qemu-img create -f qcow2 n1.qcow2 20G
qemu-nbd -c /dev/nbd0 n1.qcow2
k3os/install.sh --config n1.yml /dev/nbd0 k3os-amd64.iso
qemu-nbd -d /dev/nbd0
virsh define --file n1.xml
virsh start k3os-n1

qemu-img create -f qcow2 n2.qcow2 20G
qemu-nbd -c /dev/nbd0 n2.qcow2
k3os/install.sh --config n2.yml /dev/nbd0 k3os-amd64.iso
qemu-nbd -d /dev/nbd0
virsh define --file n2.xml
virsh start k3os-n2

scp -i /home/pineman/.ssh/id_ed25519 -o StrictHostKeyChecking=no rancher@192.168.122.10:/etc/rancher/k3s/k3s.yaml .
sed -i 's/127.0.0.1/192.168.122.10/g' k3s.yaml
export KUBECONFIG=k3s.yaml
kubectl get nodes
kubectl get po -A
