#!/bin/bash

ARCHIVE=/mnt/Archive

# Home backup
youtube-dl -j --flat-playlist 'https://www.youtube.com/playlist?list=PLI89Mvc1S1ws6TloLOnK_ecArjdr1o8ac' | jq -r '.title' > /home/pineman/Music/playlist/nostalgia-$(date +%s).txt
youtube-dl -j --flat-playlist 'https://www.youtube.com/playlist?list=PLI89Mvc1S1wsk07ms8dz_M8_C1ft2s6A6' | jq -r '.title' > /home/pineman/Music/playlist/getfcked-$(date +%s).txt
rsync -aqzhL --delete-after /home/pineman/Documents /home/pineman/Pictures /home/pineman/Music "$ARCHIVE"
# Downloads could be a simple rsync one way too.
mv /home/pineman/Videos/* "$ARCHIVE/Videos/"

# Windows backup
sudo borg create --read-special -v --stats --compression zstd "$ARCHIVE/Borg::windows-$(date -I)" /dev/sda3

# Linux backup
yay -Qqs > /home/pineman/code/pkg/pkglist.txt
yay -Qqs > /home/pineman/.pkglist.txt
sudo borg create -v --stats --compression zstd "$ARCHIVE/Borg::code-$(date -I)" /home/pineman/code/git /home/pineman/code/pkg
sudo borg create -v --stats --compression zstd "$ARCHIVE/Borg::etc-$(date -I)" /etc
