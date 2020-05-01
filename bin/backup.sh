#!/bin/bash
#set -euxo pipefail
set -x

ARCHIVE=/mnt/Archive

youtube-dl -j --flat-playlist 'https://www.youtube.com/playlist?list=PLI89Mvc1S1ws6TloLOnK_ecArjdr1o8ac' | jq -r '.title' > /home/pineman/Music/playlist/nostalgia-$(date +%s).txt
youtube-dl -j --flat-playlist 'https://www.youtube.com/playlist?list=PLI89Mvc1S1wsk07ms8dz_M8_C1ft2s6A6' | jq -r '.title' > /home/pineman/Music/playlist/getfcked-$(date +%s).txt
find /home/pineman/Music | gzip > /home/pineman/Music/music_filelist-$(date +%s).txt.gz
mv /home/pineman/Videos/* "$ARCHIVE/Archive/Videos/" || true
rsync -aqzzh --delete-after /home/pineman/Documents /home/pineman/Pictures /home/pineman/Music /home/pineman/code "$ARCHIVE"
# Downloads are not synced on purporse - its temp storage that I manually organize

sudo rsync -aqzzh --delete-after /etc "$ARCHIVE/OS Images/"
pacman -Qqs > /home/pineman/code/pkg/pkglist-$(hostname).txt
pacman -Qqs > /home/pineman/.pkglist-(hostname).txt

find /mnt/Archive | gzip > /mnt/Archive/list/archive_filelist-$(date +%s).txt.gz
find /home/pineman | gzip > /mnt/Archive/list/home_filelist-$(date +%s).txt.gz

# Offsite backup of most important stuff - docs and pics
#rclone a borg repo?
#duplicacy?
