from os import system
from time import sleep
from sys import argv

def color_test(term):
	if term == 'xterm':
		for i in range(257):
			system('echo -e "\e[38;5;{0}m████████████████████\e[0m {0}"'.format(i))
			system('echo -e "\e[48;5;{0}m                                                                               \e[0m {0}"'.format(i))
			sleep(0.04)
	else:
		for i in range(257):
			system('echo -e "\e[1;{0}m||||||||||||||||||||||||||||||||\e[0m {0}"'.format(i))
			sleep(0.04)

#color_test(argv[1])
color_test('xterm')
