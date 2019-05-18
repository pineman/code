"""
Read some file formatted as '[<float>, <float>, ... ]' in one line
(excluding ticks) into a python list of floats and convert it to a Counter
of rounded floats with precision PREC. Plot the distribution of the values.
"""

from collections import Counter
import matplotlib.pyplot as plt

r = []
with open('results.txt', 'r') as f:
    r = eval(f.readline())

from statistics import mean, median, stdev
from numpy import percentile
s1 = f"Time (mean ± σ):    {mean(r):.4} s ± {stdev(r):.4} s"
s2 = f"p95: {percentile(r, 95):.4}, p99: {percentile(r, 99):.4} s"
s3 = f"Range (min … max):  {min(r):.4} s … {max(r):.4} s"

PREC = 3
c = Counter((round(a, PREC) for a in r))
N = len(c)
x = [i for i in c.keys()]
y = [i/N for i in c.values()]

plt.bar(x,y,10**(-PREC))
plt.grid(True)
plt.annotate(s1, xy=(0.05, 0.95), xycoords='axes fraction')
plt.annotate(s2, xy=(0.05, 0.90), xycoords='axes fraction')
plt.annotate(s3, xy=(0.05, 0.85), xycoords='axes fraction')
plt.savefig('results.png')
plt.show()
