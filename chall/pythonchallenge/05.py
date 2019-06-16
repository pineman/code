import requests
import pickle

m = pickle.loads(requests.get('http://www.pythonchallenge.com/pc/def/banner.p').content)
for s in m:
    for t in s:
        print(t[0] * t[1], end='')
    print()