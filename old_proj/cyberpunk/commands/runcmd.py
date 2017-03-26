#!/usr/bin/env python3

"""
Run the command sent from prompt.parsecommand()
"""


import os
import sys
from gamesettings import *


GAME_DIR = sys.path[0]
GAME_FILESYS = os.path.join(sys.path[0], 'filesystem')
GAME_DIRLIST = [GAME_FILESYS]
for roots, dirs, _ in os.walk(GAME_FILESYS):
	for dir in dirs:
		GAME_DIRLIST.append(os.path.join(roots, dir))


def ls(args):
	if len(args) != 0:
		try:
			if len(args) == 1:
				for arg in args:
					os.system('ls ' + arg)

			elif len(args) > 1:
				for arg in args:
					print("{0}:".format(arg))
					os.system('ls ' + arg)
		except Exception:
			for arg in args:
				print('-shell: ls: {0}: No such file or directory'.format(arg))
	else:
		os.system('ls')


def cd(args):
	if not args:
		os.chdir(os.path.join(GAME_DIR, 'filesystem/home/{0}'.format(USER)))
	else:
		dir = args[0]
		if dir.startswith('/'):
			dir = os.path.join(GAME_FILESYS, dir[1:])
			# dir[1:] since dir starts with '/'. that messes os.path.join()
		try:
			previous_dir = os.getcwd()
			os.chdir(dir)
			if os.getcwd() not in GAME_DIRLIST:
				os.chdir(previous_dir)

		except Exception:
			print('-shell: cd: {0}: No such file or directory'.format(args[0]))


def pwd(args):
	currentdir = os.getcwd()
	print(currentdir)
	# print(currentdir[15:])


def read(args):
	if args:
		os.system('cat {0}'.format(args[0]))
	else:
		print('-shell: read: No file passed')


def runcmd(cmd, args):
	exec('eval(cmd)(args)')


if __name__ == "__main__":
	pass
