#!/usr/bin/env python3

"""
    17.1. threading
    17.2. multiprocessing
    17.4. concurrent.futures
    18.3. select
    18.5. asyncio
"""

#from multiprocessing.pool import ThreadPool as Pool
from multiprocessing.pool import Pool
from time import time
from urllib.request import urlopen

urls = [
        "https://www.google.com",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://www.amazon.com",
        "https://www.facebook.com"
       ]

def fetch_url(url):
    try:
        response = urlopen(url)
        return url, response.read(), None
    except Exception as e:
        return url, None, str(e)

start = time()
results = Pool().imap(fetch_url, urls)
for url, html, error in results:
    if error is None:
        print("{}: Fetched in {} seconds".format(url, time() - start))
    else:
        print("{}: Error fetching {}".format(url, error))

print("Total elapsed Time: {}".format(time() - start))
