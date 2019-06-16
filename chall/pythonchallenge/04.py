import requests
import re

n = 12345
#n = 3875
#n = 66831 # solution is peak.html
while True:
    s = requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={n}').text
    print(s, '\n')
    match = re.findall(r'and the next nothing is (\d+)', s)
    if match:
        n = int(match[0])
    else:
        print(s)
        n //= 2
