#!/usr/bin/env python3


import curses
import time
import os
import threading

screen = curses.initscr()
dimensions = screen.getmaxyx()

max_y = dimensions[0] - 1
max_x = dimensions[1] - 1

center_y = int(dimensions[0]/2)
center_x = int(dimensions[1]/2)




def main():

    quite = threading.Thread(target=putquite)
    rather = threading.Thread(target=putrather)

    quite.start() ; rather.start()



    # Stuff to make sure the terminal we ran on is back to it's original state.
    def lel(stdscr):
        # Clear screen
        stdscr.clear()

        # This raises ZeroDivisionError when i == 10.
        for i in range(0, 11):
            v = i-10
            stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

        stdscr.refresh()
        stdscr.getkey()

    while True:
        if not quite.is_alive() and not rather.is_alive():
            curses.wrapper(lel)



def putquite():
    string = 'Quite!'
    length = len(string)
    quite = curses.newwin(1, max_x, center_y, 1)
    for x in range(dimensions[1] - length -1):
        quite.addstr(0, x, string)
        quite.refresh()
        time.sleep(0.025)
        quite.clear()


def putrather():
    string = 'Rather!'
    length = len(string)
    rather = curses.newwin(max_y, length, 1, int(center_x - length/2))
    for y in range(max_y - 1):
        rather.addstr(y, 0, string)
        rather.refresh()
        time.sleep(0.10)
        rather.clear()
"""

def test():
    screen = curses.initscr()
    screen.addstr(0, 0, 'This is an application!')
    screen.addstr(1, 0, 'Hooray!')
    screen.refresh()
    time.sleep(2)
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    # Stuff to make sure the terminal we ran on is back to it's original state.
    """
if __name__ == "__main__":
	main()

"""
while True:
    if not quite.is_alive() and not rather.is_alive():
        screen.clear()
        screen.addstr(0, 0, "Press <Enter> to exit")
        screen.refresh()
        screen.getch()
        curses.endwin()
        os.system("clear")
        break
"""
