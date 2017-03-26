#!/bin/sh
if [ "$TERM" = "linux" ]; then
  /bin/echo -e "
  \e]P02d2d2d
  \e]P1f2777a
  \e]P299cc99
  \e]P3ffcc66
  \e]P46699cc
  \e]P5cc99cc
  \e]P666cccc
  \e]P7d3d0c8
  \e]P8747369
  \e]P9f2777a
  \e]PA99cc99
  \e]PBffcc66
  \e]PC6699cc
  \e]PDcc99cc
  \e]PE66cccc
  \e]PFf2f0ec
  "
  # get rid of artifacts
  clear
fi
