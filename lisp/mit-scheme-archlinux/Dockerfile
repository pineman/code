FROM archlinux:latest
RUN pacman -Syyu --noconfirm base-devel git \
 && useradd -m -U -G wheel pineman \
 && echo '%wheel ALL=(ALL:ALL) NOPASSWD: ALL' > /etc/sudoers.d/wheel
USER pineman
WORKDIR /home/pineman
RUN git clone --depth 1 https://aur.archlinux.org/mit-scheme.git \
 && cd mit-scheme \
 && gpg --keyserver hkps://keys.openpgp.org/ --recv-keys 8F664EF430167B808170D35AC9E40BAAFD0CB132 \
 && makepkg -si --noconfirm

