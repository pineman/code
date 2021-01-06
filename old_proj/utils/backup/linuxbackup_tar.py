#!/usr/bin/env python3
"""
Makes a backup of the whole system, including /home, using tar.
TO DO: Make this a command line tool, using argparse.
Overhaul this old shit.
"""


import os
from pwd import getpwuid
import time
import sys
import readline

# Get the user's name, for various things.
user = getpwuid(os.getuid())[0]

# Script path.
SCRIPT_PATH = str(os.path.abspath(__file__)).replace(" ", "\\ ")

SCRIPT_DIR = str(os.path.dirname(os.path.abspath(__file__)))

# Declare the variable backup_path as global.
backup_path = ''

# Variables for backup name.
DISTRO = ""
DATE = ""


# Function that retrieves those.
def getvariables():
    # Distro
    os.system("cat /etc/*-release | grep PRETTY_NAME > distro.txt")
    with open("distro.txt", "r") as distro:
        for line in distro.readlines():
            global DISTRO
            DISTRO = line.replace("PRETTY_NAME=", "").rstrip()
            DISTRO = DISTRO.replace("\"", "")
            DISTRO = DISTRO.replace(" ", "-")
    os.system("rm distro.txt")
    # Date
    global DATE
    DATE = time.strftime("%d-%m")


# In case the script is not run in a terminal, make it so.
def runinterminal():
    if not sys.stdin.isatty():
        # This runs the script in xterm, passing the argument 'noterminal'.
        # This argument is later used in the function 'noterminal',
        # to warn the user the script needs to be run in a terminal.
        options = "-bc -fa monospace -bg rgb:40/40/40 -fg rgb:E8/E8/E8"
        os.system("xfce4-terminal -x " + SCRIPT_PATH + "" + " noterminal")
    else:
        return False


# Function to ask the user for backup_path.
def askforpath():

    global backup_path

    print()
    print("Enter the path you want to back up to.")
    backup_path = input('>>> ')
    backup_path = backup_path.strip()
    print()

    # Sweet tricks, boy
    if backup_path.startswith('~/'):
        backup_path = backup_path.replace('~/', '/home/' + user + '/')


# Main function that interacts with the user.
def backup():
    global backup_path

    # Open up the exclusions file.
    with open(SCRIPT_DIR + "/exclude.txt", "r") as excludefile:
        excludefile = excludefile.readlines()

    exclude = ""
    for exclusion in excludefile:

        if exclusion.startswith('~/'):
            exclusion = exclusion.replace('~/', '/home/' + user + '/')

        if " " in exclusion:
            exclude = exclude.replace(' ', '\ ')
        exclude += exclusion

    print("This script performs a backup of the whole system (e.g. ' /* ').")
    print("The following paths are excluded:")
    print(exclude)
    print("You can modify them by editing the included exclude.txt file.")

    # Check if arguments have been passed.
    # Paths passed as an argument need to be between quotes.
    if len(sys.argv) == 2:
        if 'noterminal' not in sys.argv[1]:
            backup_path = sys.argv[1].strip()

            if backup_path.startswith('~/'):
                backup_path = backup_path.replace('~/', '/home/' + user + '/')

        else:
            askforpath()

    elif len(sys.argv) >= 3:
        askforpath()

    else:
        askforpath()

    time.sleep(2)

    # Check if backup_path is correct.
    print()
    print("To review, /* will be backed up to:")
    print(backup_path)
    print("Is that okay? [y/n]")
    # Ask the user.
    decision = input('>>> ').strip().lower()

    # If it is correct, let's start the backup.
    decided = False
    if decision.startswith('y'):
        decided = True

    # If it isn't, let's ask again, untill the user has decided.
    else:
        while not decided:
            askforpath()
            print("To review, /* will be backed up to:")
            print(backup_path)
            print("Is that okay? [Y/n]")
            decision = input('>>> ').strip().lower()
            if decision.startswith('y'):
                decided = True
                break

    # If we got here, it means the user has (finally) dicided on a path,
    # and we can start the backup.
    print("Backup process will start now.")
    time.sleep(1)

    # Get variables for backup name
    getvariables()

    # Change directories to backup_path
    try:
        os.chdir(backup_path)
    except IOError:
        os.makedirs(backup_path)
        os.chdir(backup_path)

    # Run tar in the desired directory.
    os.system("sudo tar --exclude=/home/pineman/{0}-{1}.tar.gz --exclude-from=" + SCRIPT_DIR.replace(" ", "\\ ") + "/exclude.txt" + " -czvpf {0}-{1}.tar.gz /".format(DISTRO, DATE))

    # Run notification to inform the user the backup has finished.
    os.system('notify-send -i terminal "Backup" "Backup has finished."')

# Function that tells the user the script needs to be ran in a terminal,
# only in case he/she didn't do so (i.e., the script ran in xterm automatically).
def noterminal():
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'noterminal':
            print("Script ran a terminal automatically. It needs to run in one.")


# Main loop
def main():
    runinterminal()
    noterminal()
    backup()


# Fire it up! #################################################################
if __name__ == '__main__':
	main()
	#getvariables()
