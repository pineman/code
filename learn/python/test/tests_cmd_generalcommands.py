"""
Initial prototype for super cyberpunk text-based game!
"""

import cmd
import curses
import os
import sys
import curses_starting

GAME_DIR = sys.path[0]

# Strategy is to use cmd for the main 'terminal' in which the player resides,
# and to make special programs such as e-mail, browsers, IRC clients, and the
# like, in curses.
# Initialize cmd Class with commands such as 'ls', 'cd', 'cat', 'rm', 'mkdir'


class Terminal(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        os.system('clear')

    prompt = '[pineman@leethaxor]$ '
    intro = "You're now ingame!"

    def do_runapp(self, args):
        curses_starting.test()

    def do_cd(self, folder):
        if folder.startswith('/'):
            os.chdir(GAME_DIR + '/filesystem' + folder)
        if not folder:
            os.chdir(GAME_DIR + '/filesystem/home/pineman')
        else:
            os.chdir(folder)
        print(os.getcwd()[13:])

    def do_ls(self, folder):
        if not folder:
            os.system('ls')
        else:
            os.system('ls ' + folder)

    def do_cat(self, file1, file2=None):
        if file2 is None:
            os.system('cat ' + file1)
        else:
            os.system('cat ' + file1 + ' ' + file2)

    def do_pwd(self, args):
        print(os.getcwd()[13:])

    def do_exit(self, exit):
        return True

Terminal().cmdloop()
