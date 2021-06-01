#!/bin/bash
set -euxo pipefail

# https://openzfs.github.io/openzfs-docs/Getting%20Started/Debian/Debian%20Buster%20Root%20on%20ZFS.html
apt install -y debootstrap gdisk dkms dpkg-dev linux-headers-$(uname -r)
apt install -y -t buster-backports --no-install-recommends zfs-dkms
modprobe zfs
apt install -y -t buster-backports zfsutils-linux
DISK=/dev/vda
sgdisk --zap-all $DISK
sgdisk -a1 -n1:24K:+1000K -t1:EF02 $DISK
sgdisk -n2:1M:+512M -t2:EF00 $DISK
sgdisk -n3:0:+1G -t3:BF01 $DISK
sgdisk -n4:0:0 -t4:BF00 $DISK
zpool create \
  -o cachefile=/etc/zfs/zpool.cache \
  -o ashift=12 -d \
  -o feature@async_destroy=enabled \
  -o feature@bookmarks=enabled \
  -o feature@embedded_data=enabled \
  -o feature@empty_bpobj=enabled \
  -o feature@enabled_txg=enabled \
  -o feature@extensible_dataset=enabled \
  -o feature@filesystem_limits=enabled \
  -o feature@hole_birth=enabled \
  -o feature@large_blocks=enabled \
  -o feature@lz4_compress=enabled \
  -o feature@spacemap_histogram=enabled \
  -o feature@zpool_checkpoint=enabled \
  -O acltype=posixacl -O canmount=off -O compression=lz4 \
  -O devices=off -O normalization=formD -O relatime=on -O xattr=sa \
  -O mountpoint=/boot -R /mnt \
  bpool ${DISK}3
zpool create \
  -o ashift=12 \
  -O acltype=posixacl -O canmount=off -O compression=lz4 \
  -O dnodesize=auto -O normalization=formD -O relatime=on \
  -O xattr=sa -O mountpoint=/ -R /mnt \
  rpool ${DISK}
zfs create -o canmount=off -o mountpoint=none bpool/BOOT
zfs create -o mountpoint=/boot bpool/BOOT/debian
zfs create -o canmount=off -o mountpoint=none rpool/ROOT
zfs create -o canmount=noauto -o mountpoint=/ rpool/ROOT/debian
zfs mount rpool/ROOT/debian
zfs create rpool/home
mkdir /mnt/run
mount -t tmpfs tmpfs /mnt/run
mkdir /mnt/run/lock
debootstrap buster /mnt
mkdir /mnt/etc/zfs
cp /etc/zfs/zpool.cache /mnt/etc/zfs/
IFACE=enp1s0
echo "auto $IFACE
iface $IFACE inet dhcp" > /mnt/etc/network/interfaces.d/$IFACE
echo 'deb http://deb.debian.org/debian buster main contrib
deb-src http://deb.debian.org/debian buster main contrib

deb http://security.debian.org/debian-security buster/updates main contrib
deb-src http://security.debian.org/debian-security buster/updates main contrib

deb http://deb.debian.org/debian buster-updates main contrib
deb-src http://deb.debian.org/debian buster-updates main contrib' > /mnt/etc/apt/sources.list
echo 'deb http://deb.debian.org/debian buster-backports main contrib
deb-src http://deb.debian.org/debian buster-backports main contrib' > /mnt/etc/apt/sources.list.d/buster-backports.list
echo 'Package: libnvpair1linux libuutil1linux libzfs2linux libzfslinux-dev libzpool2linux python3-pyzfs pyzfs-doc spl spl-dkms zfs-dkms zfs-dracut zfs-initramfs zfs-test zfsutils-linux zfsutils-linux-dev zfs-zed
Pin: release n=buster-backports
Pin-Priority: 990' > /mnt/etc/apt/preferences.d/90_zfs
mount --rbind /dev /mnt/dev
mount --rbind /proc /mnt/proc
mount --rbind /sys /mnt/sys
chroot /mnt /usr/bin/env DISK=$DISK bash --login
