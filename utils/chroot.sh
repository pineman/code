arch=/data/local/arch
img=/storage/sdcard1/archlinuxarm.img
loopdev=/dev/block/loop250
 
hostname aquaris
mknod $loopdev b 7 250
losetup $loopdev $img
mount -t ext4 $loopdev $arch
mount -t devpts /dev/pts $arch/dev/pts
mount -o bind /dev $arch/dev
mount -t proc /proc $arch/proc
mount -t sysfs /sys $arch/sys
chroot $arch /bin/bash
