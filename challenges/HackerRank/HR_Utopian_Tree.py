#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/utopian-tree

def treeheight():
	growthcycle = int(input('Input the number of growthcycles:\n>>>'))
	treesize = 1
	
	if growthcycle % 2 != 0:
		for n in range(int((growthcycle-1)/2)):
			treesize *= 2
			treesize += 1
		treesize *= 2
		
	else:
		for n in range(int(growthcycle/2)):
			treesize *= 2
			treesize += 1
			
	return treesize

def main():
	numberoftests = int(input('Input the number of tests to do:\n>>>'))
	treeheights = {}
	test = 1
	
	for x in range(numberoftests):
		treeheight_temp = treeheight()
		treeheights.update({test:treeheight_temp})
		test += 1
	
	test = 1
	for x in range(numberoftests):
		print('The height of the tree is: ' + str(treeheights[test]))
		test += 1

if __name__ == "__main__":
	main()
