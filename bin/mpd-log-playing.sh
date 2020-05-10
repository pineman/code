#!/bin/bash
while true
do
  cat <(echo -n $(date +"[%d/%m/%Y %H:%M:%S]") '') <(mpc current) >> ~/Documents/Music/mpd-playing.log
  mpc idle player
done
