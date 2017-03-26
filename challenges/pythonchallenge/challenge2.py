#!/usr/bin/env python3

import requests

r = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')

raw = r.text.split('\n')

string = str(raw[37:-3])

found = ''

for char in string:
	if char not in found:
		found += char

for char in found:
	print('{0}: {1}'.format(char, string.count(char)))
