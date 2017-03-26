import timeit
import os
import sys

f = open(os.devnull, 'w')
sys.stdout = f

var = 0
def giver():
	global var
	var = 100 / 5

def taker():
	print(var)

giver()

print(timeit.timeit("taker()", setup="from __main__ import taker", number=10000000), file=sys.stderr)
