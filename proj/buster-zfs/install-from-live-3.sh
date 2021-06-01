mount | grep -v zfs | tac | awk '/\/mnt/ {print $3}' | \
  xargs -i{} umount -lf {}
zpool export -a
systemctl poweroff

