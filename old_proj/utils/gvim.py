import subprocess
import time
import sys


def getdate():
	hour = time.localtime().tm_hour

	if hour in range(8, 18):
		# Use Light theme.
		return '/home/pineman/.vimrc_light'
	else:
		# Use Dark theme.
		return '/home/pineman/.vimrc_dark'


def runvim():
	theme = getdate()
	with open('/home/pineman/log', 'a') as log:
		for thing in sys.argv:
			log.write(thing + '\n')

	if len(sys.argv) >= 3:
		subprocess.call(['gvim_orig', '-u', theme, sys.argv[2]])
	else:
		subprocess.call(['gvim_orig', '-u', theme])


def main():
	runvim()


if __name__ == "__main__":
	main()
