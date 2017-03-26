#!/usr/bin/env python3          
# Tasty shebang

# Bravest of Sir Knights
# By João Pinheiro and Rodrigo Serrão
# Story and dumb stuff by Guilherme Ramos (aka Interface)

# Le Guilherme Ramos >> Le Sir Knight Gui
# Le João Pinheiro >> Le Sir Knight Pine
# Le Rodrigo Serrão >> Le Sir Knight Rojer
# Le Diogo Tito >> Le Sir Knight Titus

###############################################################################
# main imports

# import those nice classes ;)
# first use "os" module and "sys" module to get the path were they lay
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

# import the player class
from oldClasses import Player
from oldClasses import StatAssigner

# GUI  (nonexistant)
#from tkinter import *
#from tkinter import ttk

# Random events
import random

# Load/Save data
import json

# Get those dramatic pauses
import time

###############################################################################

# main setup; find out if this is the first time the player runs the game
# act accordingly

try:
    f = open("settings.bosk", "r+")
    exec(f.readline())
except FileNotFoundError:
    f = open("settings.bosk", "w")
    a = f.write("first_time = False")
    f.close()
    first_time = True
    
    
# run an intro if this is the first time the player runs the game
# ask to load a file otherwise

if first_time:
    pass
else:
    print("Do you want to load your game progress?")
    d = input(">> ").strip().lower()
    if not(d.startswith("n")):
        print("You can exit the loading process whenever you may need, "\
              "by typing <quit>")
        while True:
            file = input("FileName >> ").strip().lower()
            if file == "quit":
                break
            try:
                with open(file + ".save", "r") as f:
                    #process that loaded data
                    break
            except FileNotFoundError:
                print("There is no Data file called <" + file + ">")
                
###############################################################################

# Important functions

# Clear screen function, prints nothing for 40 lines
# very handy (Pineman)

def clear(x=40):
    for n in range(x):
        print()
        
# Line break fuction
def br():
    print()

# Sleep function, so as to allow the player to read text
# also very handy (Pineman)

debugging = True

def sleep(t=4):
    # when we are debugging, really annoying having to wait... use this
    #to bypass that. when we finish it, clear these 2 lines and the variable
    #in the beginning of the file 
    # (I've put the variable over here so it's easier!)
    # agreed, nice one
    if debugging:
        return
    time.sleep(t)
    
#not working yet
'''
def save_player(player):
    while True:
        print("Please type in the name of the file to which you would like to "\
        "save:")
        file = input(">> ").strip().lower()
        with open(file+".pl", "w") as f:
            f.write(json.dumps(player.get_data()))
'''

###############################################################################

# Map section

"""
map = [
[1, 2, 3, 4, 5, 6],
[7, 8, 9, 10, 11, 12]
]
"""

# ppx = 
# x value of the player's position
# ppy = 
# y value of the player's position
# map[ppx][ppy]
#
# e.g.
# if player goes north
#   ppx = ppx
#   ppy -= 1
#
# We wil need to always keep track of both of these variables ppy and ppx.
# This will allow us to implement the "go" command, like so:
# -> I'm a noob so this is not the correct syntax obviously. <-
# def go_north:
#   ppy -= 1
# def go_south:
#   ppy += 1
#
# Or maybe even like a command that takes an argument:
# go <direction> (north, east, south, west)
#
# Then, once we have the player's position, we can define what happens in said
# position of the map.
# Maybe we could define every little piece of the map individually,
# like in FPSes or other games.
# So we would have to define map[0][0], map[0][1]...
# (Maybe there's a better way.)
# With this method we can also "remember" what the player did in each single
# instance of the map. This is useful as the player may come back to a part of
# the map, to speak to an NPC again or find a new solution for that part.

###############################################################################

print("Welcome to...")

sleep(1)

print("""
BBBBBBBBBBBBBBBBB        OOOOOOOOO        SSSSSSSSSSSSSSS KKKKKKKKK    KKKKKKK
B::::::::::::::::B     OO:::::::::OO    SS:::::::::::::::SK:::::::K    K:::::K
B::::::BBBBBB:::::B  OO:::::::::::::OO S:::::SSSSSS::::::SK:::::::K    K:::::K
BB:::::B     B:::::BO:::::::OOO:::::::OS:::::S     SSSSSSSK:::::::K   K::::::K
  B::::B     B:::::BO::::::O   O::::::OS:::::S            KK::::::K  K:::::KKK
  B::::B     B:::::BO:::::O     O:::::OS:::::S              K:::::K K:::::K   
  B::::BBBBBB:::::B O:::::O     O:::::O S::::SSSS           K::::::K:::::K    
  B:::::::::::::BB  O:::::O     O:::::O  SS::::::SSSSS      K:::::::::::K     
  B::::BBBBBB:::::B O:::::O     O:::::O    SSS::::::::SS    K:::::::::::K     
  B::::B     B:::::BO:::::O     O:::::O       SSSSSS::::S   K::::::K:::::K    
  B::::B     B:::::BO:::::O     O:::::O            S:::::S  K:::::K K:::::K   
  B::::B     B:::::BO::::::O   O::::::O            S:::::SKK::::::K  K:::::KKK
BB:::::BBBBBB::::::BO:::::::OOO:::::::OSSSSSSS     S:::::SK:::::::K   K::::::K
B:::::::::::::::::B  OO:::::::::::::OO S::::::SSSSSS:::::SK:::::::K    K:::::K
B::::::::::::::::B     OO:::::::::OO   S:::::::::::::::SS K:::::::K    K:::::K
BBBBBBBBBBBBBBBBB        OOOOOOOOO      SSSSSSSSSSSSSSS   KKKKKKKKK    KKKKKKK
""")

sleep(1)

print("""             
			Bravest of Sir Knights, """)
sleep(1)
print("			   v0.1.2 very alpha, such development") #YEAH!

sleep(1)
clear(3)

input("Press Enter to continue!")

# Cool "Loading" snippet by Sir Knight Rojer ;)
# Gives that "pro" effect ;)

beg = time.time()
end = beg + 2
l = ["|Loading   ", "/Loading.  ", "-Loading.. ", "\\Loading..."]
while time.time() < end:
    for i in l:
        sleep(0.1)
        print(i, end="\r")
        
###############################################################################

clear()

# Start defining the player
# Name input. Run while user doesn't accept inputed name

done = False
while not done:
    print("Please input your name, Brave Sir Knight")
    name = input(">> ").strip()
    if name == "":
        #no need for name.isspace() >> .strip() takes care of it
        # very nice  -Pineman
        continue
    print("Is your name " + name + "? [y/n]")
    decision = input(">> ").strip().lower()
    if decision.startswith("y") and len(name) > 0:
        done = True

print()
print("You now are this guy: " + name)

sleep(2)

# Sex input. Similar to name input
clear(3)

sexes = ["male","female"]
print("Please input your sex, Brave Sir Knight [male/female]")
while True:
    sex = input(">> ").strip().lower()
    if sex in sexes:
        print("Are you " + sex + "? [y/n]")
        decision = input(">> ").strip().lower()
        if decision.startswith("y"):
            break
    print("Please input your sex by writing \"male\" or \"female\"")
    

# Define the player_full_name
# Var that depends on the player's sex and name:

if sex == "female":
    player_full_name = "Brave Sir Knightress " + name
    print("What? A girl? Great Scott!")    ## Everyone knows girls don't exist
    print("Nonetheless, welcome, " + player_full_name + ".")
    
elif sex == "male":
    player_full_name = "Brave Sir Knight " + name
    print("Welcome, " + player_full_name + ".")
    
sleep(1.5)

###############################################################################

# Instructions (Talvez mais tarde um minitut)
# print("Here are the instructions for playing, " + player_full_name)

###############################################################################

# Stat attribution! + Player() creation
p = Player(name=player_full_name, sex=sex)
StatAssigner(player_full_name, first=True, tokens=15, player=p).cmdloop()
###############################################################################
# Intro skip? I'm tired. Help, brave sir knight!

print("Do you wish to skip the intro?")
skipdecision = input(">> ").strip().lower()
if not(skipdecision.startswith("y")):
	clear()
	sleep(1)
	print("You wake up to see yourself surrounded by nothing but cave walls.")
	sleep()
	print("You do not recall the events of the past couple of days.")
	sleep()
	print("You arrived on this land two nights ago, by boat,")
	sleep()
	print("and rested one of the nigthts in Port Hankerl, to the south of your location.")
	sleep()
	br()
	print("Before heading out, you eat your last provision, and round up your things:")
	### INVENTORY-LIST
	br()
	print("You are in the middle of Nowhere Forest, without any tasks at hand,")
	sleep()
	print("but with one goal: to wander the land in search for adventure,")
	sleep()
	print("so as to earn the title of Bravest of Sir Knight!")
	sleep()
	clear(3)
else:
	br()


input("That's all, folks!")
while True:
    try:
        exec(input())
    except Exception:
        pass
