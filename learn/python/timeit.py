import timeit
import os
import sys

f = open(os.devnull, 'w')
sys.stdout = f

def taker():
	var = 100 / 5
	print(var)

print(timeit.timeit("taker()", setup="from __main__ import taker", number=10000000), file=sys.stderr)
