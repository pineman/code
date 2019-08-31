qemu-system-x86_64 -drive file=/dev/sda,format=raw -m 4G -smp 3 -cpu host -machine type=pc,accel=kvm -L . -bios /usr/share/ovmf/x64/OVMF_CODE.fd
