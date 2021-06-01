#!/bin/bash
set -euxo pipefail

ln -s /proc/self/mounts /etc/mtab
apt update
apt install -y console-setup locales
dpkg-reconfigure locales tzdata keyboard-configuration console-setup
apt install -y dpkg-dev linux-headers-amd64 linux-image-amd64
apt install -y zfs-initramfs
echo REMAKE_INITRD=yes > /etc/dkms/zfs.conf
apt install -y grub-pc
apt remove -y --purge os-prober
passwd
echo '[Unit]
DefaultDependencies=no
Before=zfs-import-scan.service
Before=zfs-import-cache.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/sbin/zpool import -N -o cachefile=none bpool
# Work-around to preserve zpool cache:
ExecStartPre=-/bin/mv /etc/zfs/zpool.cache /etc/zfs/preboot_zpool.cache
ExecStartPost=-/bin/mv /etc/zfs/preboot_zpool.cache /etc/zfs/zpool.cache

[Install]
WantedBy=zfs-import.target' > /etc/systemd/system/zfs-import-bpool.service
systemctl enable zfs-import-bpool.service
cp /usr/share/systemd/tmp.mount /etc/systemd/system/
systemctl enable tmp.mount
apt install -y popularity-contest
grub-probe /boot
update-initramfs -c -k all
vi /etc/default/grub
# Set: GRUB_CMDLINE_LINUX="root=ZFS=rpool/ROOT/debian"
vi /etc/default/grub
# Remove quiet from: GRUB_CMDLINE_LINUX_DEFAULT
# Uncomment: GRUB_TERMINAL=console
# Save and quit.
update-grub
grub-install $DISK
mkdir /etc/zfs/zfs-list.cache
touch /etc/zfs/zfs-list.cache/bpool
touch /etc/zfs/zfs-list.cache/rpool
zed -F &
read
cat /etc/zfs/zfs-list.cache/bpool
cat /etc/zfs/zfs-list.cache/rpool
read
fg
sed -Ei "s|/mnt/?|/|" /etc/zfs/zfs-list.cache/*
apt install -y openssh-server
echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
zfs snapshot bpool/BOOT/debian@install
zfs snapshot rpool/ROOT/debian@install
exit
