#!/usr/bin/env python3
"""
Script to make playlists of each folder on my music collection
"""

import os
import subprocess
import shlex


MUSIC_DIR = "/home/pineman/Music"
PLAYLIST_DIR = MUSIC_DIR + "/Playlists"


def main():
	os.chdir(MUSIC_DIR)

	roots = [root for root in os.listdir() if os.path.isdir(root) and os.listdir(root)]
	for root in roots:
		try:
			playlist = subprocess.check_output('find {0} | grep mp3'.format(shlex.quote(root)),\
											shell=True, universal_newlines=True).split('\n')
		except Exception:
			pass

		playlist_location = '{0}/{1}.m3u'.format(PLAYLIST_DIR, root)

		with open(playlist_location, 'w+') as playlist_file:
			for line in playlist:
				if line:
					playlist_file.write('/home/pineman/Music/{0}\n'.format(line))


if __name__ == "__main__":
	main()
