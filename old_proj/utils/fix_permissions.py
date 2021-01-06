"""
Script to watch and fix server persmissions for all users.

*****
TO-DO:
	Move try... except to check_permissions() and change_permissions()
"""


import subprocess
import os
import time
import pyinotify


PINEMAN = '/home/pineman/www'
OWNCLOUD = '/home/pineman/owncloud'
OWNCLOUD_DATA = '/home/pineman/data'
ALMIRO = '/home/almiro/almiro.pineman.me'
ALMIRO_DATA = '/home/almiro/data.almiro.pineman.me'

DIRS = {PINEMAN:'pineman', ALMIRO:'almiro', ALMIRO_DATA:'almiro', OWNCLOUD:'pineman', OWNCLOUD_DATA:'pineman'}


def log(logstring):
	date = sh('date +%d/%m/%Y\ %T').strip()
	with open('/home/pineman/logs/permissions.log', 'a') as logfile:
		logfile.write('[{0}] {1} \n'.format(date, logstring))
	logfile.close()


def sh(cmd):
	return subprocess.check_output(cmd, universal_newlines=True, shell=True)


def check_permissions(path):
	perms = sh('stat -c %a {0}'.format(path)).strip()

	if os.path.isdir(path):
		if perms != '770':
			return True
		else:
			return False
	else:
		if perms != '660':
			return True
		else:
			return False


def change_permissions(basepath, path):
	log('--> Changing permissions of {0}'.format(path))

	while True:
		try:
			username = DIRS[basepath]
			break
		except KeyError:
			basepath = os.path.dirname(basepath)

	sh('chown {0}:nginx {1}'.format(username, path))

	if os.path.isdir(path):
		sh('chmod 770 {0}'.format(path))
	else:
		sh('chmod 660 {0}'.format(path))


def check_events(notifier):
	notifier.process_events()
	if notifier.check_events():
		notifier.read_events()
		notifier.process_events()


def main():
	class EventHandler(pyinotify.ProcessEvent):
		def process_IN_CREATE(self, event):
			try:
				change_permissions(basepath = event.path, path = event.pathname)
			except Exception as error:
				log('--> Error changing permissions of {0}: {1}'.format(event.pathname, error))
				return 1

		def process_IN_MODIFY(self, event):
			try:
				if check_permissions(event.pathname):
					change_permissions(basepath = event.path, path = event.pathname)
			except Exception as error:
				log('--> Error changing permissions of {0}: {1}'.format(event.pathname, error))
				return 1

	wm = pyinotify.WatchManager()
	mask = pyinotify.IN_MODIFY | pyinotify.IN_CREATE | pyinotify.IN_CLOSE_WRITE

	handler = EventHandler()
	notifier = pyinotify.Notifier(wm, handler, timeout=10)

	for dir in DIRS.keys():
		wm.add_watch(dir, mask, rec=True)

	while True:
		check_events(notifier)
		time.sleep(5)


if __name__ == "__main__":
	log('Started.')
	main()
