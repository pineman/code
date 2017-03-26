#!/usr/bin/env python3

import requests
import re

r = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')

raw = r.text.split('\n')

string = str(raw[21:-2])
