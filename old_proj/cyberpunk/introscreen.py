#!/usr/bin/env python3
"""
Intro screen for Cyberpunk game.
Cool thing in curses (I hope)
"""

import curses


USER = input('Please enter your desired username.\n>>> ')
HOSTNAME = input('Please enter the name of your computer.\n>>> ')

with open('gamesettings.py', 'r') as temp:
	settings = temp.readlines()

settings[1] = "USER = '{0}'\n".format(USER)
settings[2] = "HOSTNAME = '{0}'\n".format(HOSTNAME)

with open('gamesettings.py', 'w') as temp:
	temp.writelines(settings)
	temp.close()
