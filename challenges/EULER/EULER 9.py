#!/usr/bin/env python3

def main():
	for a in range(1,1000):
		for b in range(a,1000):
			for c in range(b,1000):
				if a + b + c == 1000 and a**2 + b**2 == c**2:
					return a * b * c

if __name__ == '__main__':
	print(main())
