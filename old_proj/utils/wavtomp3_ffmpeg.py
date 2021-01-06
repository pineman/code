"""
Convert .wav files to .mp3 using ffmpeg.
TO DO: Make this a command line tool, using argparse module.
"""


import os
from pwd import getpwuid
import readline
import subprocess


# Get the user's name, for path purporses.
user = getpwuid(os.getuid())[0]

# Globals
recursive = ""
delete = ""


# Intro to the script
def intro():
    print("This script will convert all found .wav files in a path to .mp3 files.")
    print("You can choose whether to recursively check all subdirectories of that path.")
    print()


# Function to ask things!
def confirmation(question):

    print(question + " [y/n]")
    decision = input('>>> ').strip().lower()
    print()

    if decision.startswith('y'):
        return True

    else:
        return False


# Ask the user for the path where the .wav files are.
def askforpath():

    valid = False

    while not valid:

        print("Enter the path where your .wavs are.")
        wavpath = input('>>> ')
        wavpath = wavpath.strip()
        # Paths with "~/" might be troublesome.
        # I guess?

        if wavpath.startswith('~/'):
            wavpath = wavpath.replace('~/', '/home/' + user + '/')

        if not os.path.isdir(wavpath):
            print("Selected path does not exist.")
            continue

        valid = True
    return wavpath


# Convert the files, going recursively into the specified path.
def recursion():

    done = False
    while not done:
        path = askforpath()

        # Get all files under this path -- 'allfiles' list contains the real,
        # absolute path to each file under every subdirectory under the user-specified
        # path.
        allfiles = []
        for roots, _, filelists in os.walk(path):
            for filelist in filelists:
                allfiles.append(os.path.join(roots, filelist))

        # Filter the .wavs from 'allfiles' list.
        wavfiles = []
        for file in allfiles:
            # Testing for vs testing against...
            if not file[-4:] == ".wav":
                pass

            else:
                wavfile = file
                wavfiles.append(wavfile)

        # Let's pass the .wavs onto foundfiles().
        # It also checks if list is empty.
        if not foundfiles(wavfiles):
            done = False
        else:
            done = True


# Convert the files, not going recursively into the specified path!
def norecursion():

    done = False
    while not done:

        path = askforpath()

        wavfiles = []
        # List all the files in the user-specified path.
        for file in os.listdir(path):
            # Filter the .wavs.
            # It's necessary to join 'file' with 'path' because 'file' is only
            # a filename.
            # os.listdir only returns filenames.

            if os.path.isfile(os.path.join(path, file)) and file[-4:] == ".wav":
                # Now I can call 'file' 'wavfile'.
                # Append the wavfile (its full path) to 'wavfiles' list.
                wavfile = os.path.join(path, file)
                wavfiles.append(wavfile)

        # Let's pass the .wavs onto foundfiles().
        # It also checks if the list is empty.
        if not foundfiles(wavfiles):
            done = False
        else:
            done = True


def foundfiles(wavfiles):
        # 'wavfiles' is a list containing full path to (hopefully) .wav files.
        # Check if we found any .wav files in that list.
        # If we didn't (i.e. list is empty), ask for another path.
        if not wavfiles:
            if confirmation("No .wav files found. Do you wish to specify another path?"):
                return False
            else:
                return True
        # If we did, let's convert them.
        else:
            for wavfile in wavfiles:
                convert(wavfile)
            return True


def convert(wavfile):
    # Create some useful vars for naming.
    filename = os.path.basename(wavfile)
    mp3file = wavfile.replace(".wav", ".mp3")

    # Convert the files.
    print("Converting " + filename + " ...")
    subprocess.call(["ffmpeg", "-i", wavfile, "-acodec", "mp3", "-ab", "320k", mp3file, "-v", "0"])

    # Finally, if the user specified, delete the .wav.
    if delete:
        os.remove(wavfile)


# Main loop
def main():

    # Run the intro.
    intro()

    # Ask for options.
    global recursive
    global delete

    recursive = confirmation("Do you wish to check recursively?")
    delete = confirmation("Do you wish to delete the .wav files after conversion?")

    # Pretty self explanatory;
    # If we should go recursive, do that, otherwise... don't!
    if recursive:
        recursion()
        print("All done!")
    else:
        norecursion()
        print("All done!")


# Fire it up!
if __name__ == "__main__":
    main()
