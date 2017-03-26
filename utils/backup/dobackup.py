#!/usr/bin/env python3
"""
Python script to make a tar backup of the filesystem,
compress it using 'pixz' and upload it to MEGA.

TODO:
	Read settings from a conf file
	Read settings from command line arguments
"""

import subprocess
import time
from socket import gethostname
from sys import argv
import os


# Global constants
WORKDIR = '/backup'

HOSTNAME = gethostname().upper()
DATE = time.strftime('%d.%m.%Y')
FILENAME = '{0}/{1}-{2}.tpxz'.format(WORKDIR, HOSTNAME, DATE)

LOGFILE = '{0}/logs/backup-{1}.log'.format(WORKDIR, DATE)
EXCLUDE = '{0}/exclude/normal'.format(WORKDIR)

KEY = '{0}/pinecone_backup.key'.format(WORKDIR)

MAILFROM = 'root@{0}.pineman.sexy'.format(HOSTNAME.lower())
MAILTO = 'pineman@pineman.sexy'
SUBJECT = '[{0}] Backup completed at '.format(HOSTNAME)


def usage():
	print("""\
usage: dobackup [delete <int> | backup]
Commands:
	backup                     Perform a backup
	delete <int>               Delete all old backups except the <int> most recent ones
	backup-and-delete <int>    Run backup and then run delete after
	help                       Print this help message""")


# Redefine subprocess.Popen()
def system(*args, **kwargs):
	# Run the command
	proc = subprocess.Popen(*args, universal_newlines=True,
							shell=True, stdout=subprocess.PIPE,
							stderr=subprocess.STDOUT, **kwargs)
	# Log the output (stdout and stderr [stderr has been redirected to stdout])
	out = proc.communicate()[0] # communicate returns a tuple (stdout, stderr)
	if out:
		log(out)


def log(msg):
	logtime = time.strftime('%d/%m/%Y %H:%M:%S')
	logmsg = '[{0}] {1}'.format(logtime, msg)

	with open(LOGFILE, 'a+') as log:
		log.write('{0}\n'.format(logmsg))

	# Print it so journald can catch it as well
	print(logmsg)


def backup():
	log('Started.')

	log('Starting tar...')
	system('tar -Ipixz --exclude-from={0} -cpf {1} /'.format(EXCLUDE, FILENAME))
	log('Finished tar.')

	log('Encrypting...')
	system('openssl aes-256-cbc -pass file:{0} -in {1} -out {1}.enc'.format(KEY, FILENAME))
	log('Checksum is:')
	system('sha256sum {0}.enc'.format(FILENAME))
	log('Finished encrypting.')

	log('Starting megaput...')
	system('megaput --no-progress --config /root/.megarc {0}.enc'.format(FILENAME))
	log('Finished megaput.')

	log('Sending email...')
	system('gzip -kf {0}'.format(LOGFILE))

	date = subprocess.check_output(['date','-R']).decode('utf-8').strip()
	system('echo | mail -a "{0}" -r "{1}" -s "{2}{3}" "{4}"'.format(LOGFILE, MAILFROM, SUBJECT, date, MAILTO))

	log('Done.')
	system('gzip -f {0}'.format(LOGFILE))


def delete(num):
	backups = [backup for backup in os.listdir(WORKDIR) if backup.endswith('.enc')]
	backups.sort(key=lambda backup: os.path.getmtime(os.path.join(WORKDIR, backup)))

	for backup in backups[:-num]:
		os.remove(os.path.join(WORKDIR, backup))


def main():
	if argv[1] == 'backup':
		backup()

	elif argv[1] == 'delete':
		run_delete = True
	
	elif argv[1] == 'backup-and-delete':
		backup()
		run_delete = True
	
	if run_delete:
		try:
			delete(int(argv[2]))
		except IndexError:
			print("You must supply an integer with 'delete'.\n")
			usage()
		
	elif argv[1] == 'help':
		usage()
	else:
		print('unrecognized command: {0}\n'.format(argv[1]))
		usage()


if __name__ == '__main__':
	main()
