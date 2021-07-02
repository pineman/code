#!/bin/bash
# https://github.com/eoli3n/archiso-zfs
# TODO: store /boot on zfs for kernel snapshots
common_opts=(-O acltype=posixacl -O xattr=sa -O normalization=formD -O compression=lz4 -O relatime=on -O mountpoint=none -O canmount=off)
zpool create -o ashift=13 -o autotrim=on -o cachefile=/etc/zfs/zpool.cache "${common_opts[@]}" ssd /dev/disk/by-id/ata-Samsung_SSD_860_EVO_500GB_S3Z2NB0KC36879L-part2
zpool create -o ashift=12 -o cachefile=none -o altroot=/hdd "${common_opts[@]}" hdd /dev/disk/by-id/ata-ST500LM012_HN-M500MBB_S2TRJ9CCB11080
zfs create -o canmount=on -o mountpoint=/ ssd/root
zfs create -o canmount=on -o mountpoint=/home ssd/home
zfs create -o canmount=on -o mountpoint=/home/pineman/Documents ssd/Documents
systemctl enable zfs.target
systemctl enable zfs-import-cache.service zfs-mount.service zfs-import.target
zfs create -V 20G ssd/docker
mkfs.ext4 /dev/zvol/ssd/docker
mount /dev/zvol/ssd/docker /var/lib/docker
tail -1 /etc/mtab | tee -a /etc/fstab
# TODO: reboot problem com a fucking hdd pool a ser importada automaticamente
# sempre (e obvio sem altroot e por isso estraga tudo). reboots são manuais atm.
# em emergency mode:
# $ zpool export hdd
# $ exit
