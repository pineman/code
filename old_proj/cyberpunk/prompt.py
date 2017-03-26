#!/usr/bin/env python3

"""
Main terminal prompt for cyberpunk game.
"""

# Local imports

# import settings' vars, like 'USER' and 'HOSTNAME'.
# gamesettings.py
from gamesettings import *

# import list of valid commands: 'COMMANDS'.
# commands/List.py
from commands.List import *

# import runcmd function. this actually runs the commands and defines them.
# it's in a different directory for convenience.
# commands/runcmd.py
import commands.runcmd as runcmd

# Other imports
import readline
import re
import os
import sys


GAME_DIR = sys.path[0]
EXIT = False
START = True


# Define the terminal's prompt, to dynamically change it.
def prompt(currentdir):
	if currentdir == os.path.join(GAME_DIR, 'filesystem/home/' + USER):
		currentdir = '~'
	elif currentdir == os.path.join(GAME_DIR, 'filesystem'):
		currentdir = '/'
	else:
		currentdir = currentdir.split('/')[-1]
	command = input('[{0}@{1} {2}]$ '.format(USER, HOSTNAME, currentdir))
	return command


# Function that parses commands.
def parsecommand(command):
	global EXIT

	# Separate the command and arguments.
	args = command.split(' ')

	# The temp list may contain empty strings: ''
	# gotta delete them
	args = [arg for arg in args if arg]

	# Get the 'real command' and delete it from the 'args' list.
	realcmd = args[0]
	del args[0]

	# Exit command.
	if realcmd == 'exit':
		EXIT = True

	# Check if command exists.
	if realcmd not in COMMANDS:
		print('-shell: {0}: command not found'.format(realcmd))
		return False
	else:
		# If it does, return the command and a list of arguments passed.
		return realcmd, args


def main():
	while True:
		if not EXIT:
			global START
			if START:
				os.chdir(os.path.join(GAME_DIR, 'filesystem/home/' + USER))
				START = False

			currentdir = os.getcwd()
			command = prompt(currentdir)
			try:
				cmd, args = parsecommand(command)
			except Exception:
			# i.e., command was not found. parsecommand() returned False
			# and it gives like value error cause it can't assign the vars
			# 'cmd, args' to 'False'.
				continue
			# Send command and list of args to commands/runcmd.py
			runcmd.runcmd(cmd, args)
		else:
			break

if __name__ == '__main__':
	main()
