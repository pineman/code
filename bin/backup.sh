#!/bin/bash
#set -euxo pipefail
set -x

BACKUP=/backup
source $BACKUP/duplicacy_password

pacman -Q > /home/pineman/.pkglist-$(hostname).txt

# Downloads folder not synced on purporse - its temp storage that I manually organize
youtube-dl -j --flat-playlist 'https://www.youtube.com/playlist?list=PLI89Mvc1S1ws6TloLOnK_ecArjdr1o8ac' | jq -r '.title' > /home/pineman/Documents/Music/playlist/nostalgia-$(date +%d-%m-%Y).txt
youtube-dl -j --flat-playlist 'https://www.youtube.com/playlist?list=PLI89Mvc1S1wsk07ms8dz_M8_C1ft2s6A6' | jq -r '.title' > /home/pineman/Documents/Music/playlist/getfcked-$(date +%d-%m-%Y).txt
(cd /home
&& sudo -E duplicacy prune -keep 3:30
&& sudo -E duplicacy prune -keep 7:360
&& sudo -E duplicacy backup -hash -suppress CHUNK_CACHE -suppress PACK_END)
(cd /etc
&& sudo -E duplicacy prune -keep 3:30
&& sudo -E duplicacy prune -keep 7:360
&& sudo -E duplicacy backup -hash -suppress CHUNK_CACHE -suppress PACK_END)

# Offsite backup of most important stuff - Docs
# https://github.com/gilbertchen/duplicacy/wiki/Quick-Start
#(cd $BACKUP/home-duplicacy && sudo duplicacy copy -to b2 ... )
