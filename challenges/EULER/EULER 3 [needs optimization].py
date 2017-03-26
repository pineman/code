"""
EULER 3
http://projecteuler.net/problem=3
----------------------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#Lista com montes de primos

primos = [2]

for n in range(3, 10000000000, 2):
# Smart Rodrigo, refer to EULER 7.py
	roof = n**(1/2)
    for prime in primos:
        if prime > roof:
            primos.append(n)
            break
 
        if n % prime == 0:
            break
# Smart Almiro

for n in primos[::-1]:
    if 600851475143 % n == 0:
        print(n)
        break


# Dumb Pinheiro
"""
div = []

for n in primos:
    if 600851475143 % n == 0:
        div.append(n)

print(max(div))
"""

#max() manualmente
"""
a = 0
for n in div:
    if n > a:
        a = n

print(a)
"""


