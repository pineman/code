"""
EULER 6
http://projecteuler.net/problem=6
------------------------------------
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

#Child's play.
a = 0 # Sum of squares
b = 0 # Square of the sum
c = 0
for n in range(101):
	a += n**2
	c += n
b = c**2
print(b-a)
# 2 easy!



