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
from sys import argv, stdout
import os


# Global constants
WORKDIR = '/backup'
EXT = 'tpxz'

HOSTNAME = gethostname().upper()
DATE = time.strftime('%Y.%m.%d')
FILENAME = '{0}/{1}-{2}.{3}'.format(WORKDIR, HOSTNAME, DATE, EXT)
KEY = '{0}/aes-256-cbc.key'.format(WORKDIR)

LOGFILE = '{0}/logs/backup-{1}.log'.format(WORKDIR, DATE)
EXCLUDE = '{0}/exclude.txt'.format(WORKDIR)

MAILFROM = 'pineman@pineman.win'
MAILTO = 'pineman@pineman.win'
#MAILTO = 'joao.castropinheiro@gmail.com'
SUBJECT = '[{0}] Backup completed at '.format(HOSTNAME)


def usage():
    print("""\
usage: dobackup [delete <int> | backup]
Commands:
    backup                     Perform a backup
    delete <int>               Delete all old backups except the <int> most recent ones
    backup-and-delete <int>    Run backup and then run delete after
    help                       Print this help message\
    """)


# Wrapper around subprocess.Popen()
def run(*args, **kwargs):
    # Run the command
    proc = subprocess.Popen(*args, universal_newlines=True,
                            shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, **kwargs)

    # Log and return the output (stdout and stderr [stderr has been redirected to stdout])
    out = proc.communicate()[0] # communicate returns a tuple (stdout, stderr)
    if out:
        log(out)

    return proc.returncode, out


def log(msg):
    logtime = time.strftime('%d/%m/%Y %H:%M:%S')
    logmsg = f'[{logtime}] {msg}'

    with open(LOGFILE, 'a+') as logfile:
        logfile.write(f'{logmsg}\n')
        logfile.flush()

    # Print it so journald can catch it as well
    print(logmsg)
    stdout.flush()


def backup():
    log('Started.')

    # tar run as root implies -p but explicit is better than implicit
    # can also specify --one-file-system to ignore
    # /dev, /sys/, /run, /tmp and /proc but im already excluding those
    log('Starting tar...')
    r, _ = run(f'tar -Ipixz --exclude-from={EXCLUDE} --acls --xattrs -cpf {FILENAME} /')
    log(f'Finished tar. Ret: {r}.')

    log('Encrypting...')
    r, _ = run(f'openssl aes-256-cbc -e -pass file:{KEY} -in {FILENAME} -out {FILENAME}.enc')
    log(f'Finished encrypting. Ret: {r}.')

    log('sha256sum is:')
    run(f'sha256sum {FILENAME}.enc')
    log('size is:')
    run(f'du -sh {FILENAME}.enc')

    log('Uploading to mega...')
    r, _ = run(f'megaput --no-progress --disable-previews {FILENAME}.enc')
    log(f'Finished uploading. Ret: {r}')
    #if r == 0: os.remove(f'{FILENAME}.enc')
    os.remove(f'{FILENAME}.enc')

    log('Sending email...')
    _, end_time = run('date -R')
    run(f"cat '{LOGFILE}' | mail -r '{MAILFROM}' -s '{SUBJECT}{end_time}' '{MAILTO}'")

    log('Done.')
    run(f'gzip -f {LOGFILE}')


def delete(num):
    backups = [b for b in os.listdir(WORKDIR) if b.endswith('.{}'.format(EXT))]
    backups.sort(key=lambda b: os.path.getmtime(os.path.join(WORKDIR, b)))

    for b in backups[:-num]:
        os.remove(os.path.join(WORKDIR, b))


def main():
    run_delete = False
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

# vim: ts=4 sts=4 sw=4 et
