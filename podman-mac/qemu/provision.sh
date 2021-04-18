#!/bin/bash
set -euxmo pipefail

brew install podman qemu
codesign -s - --entitlements entitlements.xml --force /usr/local/bin/qemu-system-x86_64
curl -L https://app.vagrantup.com/archlinux/boxes/archlinux/versions/20210301.16394/providers/libvirt.box > arch.tar.gz
tar xzf arch.tar.gz box.img
qemu-img convert box.img -O raw arch.raw
rm arch.tar.gz box.img
qemu-system-x86_64 -drive driver=raw,file=arch.raw -cpu host -smp 1 -m 1G -machine type=q35,accel=hvf -nic user,hostfwd=tcp::23-:22 -display none &
sleep 1m
cat ~/.ssh/id_ecdsa.pub | ssh -o StrictHostKeyChecking=no -i vagrant -p 23 vagrant@localhost 'cat > ~/.ssh/authorized_keys'
ssh -o StrictHostKeyChecking=no -p 23 vagrant@localhost bash - <<EOF
sudo tee -a /etc/pacman.d/mirrorlist <<< 'Server = https://ftp.rnl.tecnico.ulisboa.pt/pub/archlinux/\$repo/os/\$arch'
sudo pacman -Syyu --noconfirm --ignore linux
sudo pacman -S podman podman-docker podman-compose --noconfirm --needed
sudo tee /etc/subuid /etc/subgid <<< 'vagrant:165536:65536'
sudo sed -i 's/driver = ""/driver = "overlay"/g' /etc/containers/storage.conf
systemctl enable --user podman.socket --now
EOF
podman system connection remove arch
podman system connection add arch --identity ~/.ssh/id_ecdsa ssh://vagrant@localhost:23/run/user/1000/podman/podman.sock
podman system connection default arch
podman info
#podman pull docker.io/ubuntu:20.10
#podman run -it docker.io/ubuntu:20.10
