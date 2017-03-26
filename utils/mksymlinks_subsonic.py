#!/usr/bin/env python3


import os


def subsonicdir(folder):
	os.chdir(os.path.join('/home/pineman/Subsonic', folder))

os.chdir('/home/pineman/Subsonic')
folders = os.listdir()
BASE = '/home/pineman/Music'
print(folders)

for artist in folders:
	os.chdir(os.path.join(BASE, artist))
	subs = [folder for folder in os.listdir() if os.path.isdir(os.path.join(os.getcwd(), folder))]
	for album in subs:
		subsonicdir(artist)
		test = os.path.join(BASE, artist)
		os.symlink(os.path.join(test, album), album)
		print(os.getcwd())
