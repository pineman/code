#!/bin/bash
while true
do
  cat <(echo -n $(date +"[%d/%m/%Y %H:%M:%S]") '') <(mpc current) >> ~/Music/mpd-playing.log
  mpc idle player
done
