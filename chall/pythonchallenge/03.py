import requests
import re

r = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')

body = ''.join(r.text.split('\n')[21:-2])

print("".join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', body)))
