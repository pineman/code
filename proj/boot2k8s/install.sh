#!/bin/bash
#https://stackoverflow.com/a/2358432
{
set -x

destroy-node() {
	virsh undefine --nvram k3os-"$1"
	virsh destroy k3os-"$1"
}
destroy-node s1
destroy-node n1
destroy-node n2
sleep 10s
curl -OL -C - https://github.com/rancher/k3os/releases/download/v0.20.6-k3s1r0/k3os-amd64.iso
modprobe nbd max_part=10
(cd k3os || exit
git checkout -- .
git apply ../mbr.patch)
# It would be better to have only one image and configure it externally.
# However due to my particular testing network config, I left it this way
create-node() {
	qemu-img create -f qcow2 "$1".qcow2 20G
	qemu-nbd -c /dev/nbd0 "$1".qcow2
	k3os/install.sh --config "$1".yml /dev/nbd0 k3os-amd64.iso
	qemu-nbd -d /dev/nbd0
	virsh define --file "$1".xml
	virsh start k3os-"$1"
}
create-node s1
create-node n1
create-node n2
until scp -i /home/pineman/.ssh/id_ed25519 -o StrictHostKeyChecking=no rancher@192.168.122.10:/etc/rancher/k3s/k3s.yaml .; do sleep 2; done
sed -i 's/127.0.0.1/192.168.122.10/g' k3s.yaml
export KUBECONFIG=k3s.yaml
kubectl get po -A
kubectl get nodes

exit
}
