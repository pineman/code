import requests


r = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')

body = r.text.split('\n')

mess = ''.join(body[37:-3])
s = ''
for c in mess:
    if c.isalpha():
        s += c
print(s)

import re
print(re.sub('[^a-z]', '', mess)) # substitute everything not [a-z] for ''

"""
from collections import Counter
for char in Counter(mess):
    print(char)
"""
"""
found = ''
for char in mess:
    if char not in found:
        found += char

for char in found:
    print('{0}: {1}'.format(char, mess.count(char)))
"""
