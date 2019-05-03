"""
EULER 4
http://projecteuler.net/problem=4
----------------------------------
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers
"""

# The biggest number obtained by multiplying two 3-digit numbers has six
# digits. 
# The smallest number obtained by the same method has 5 digits.
# Therefore the solution can either be a 5-digit or a 6-digit number.
#
# By starting backwards we would ensure less time to find the answer.
# i.e. by starting with the number 999 and work our way down, instead of
# starting at 100 and working up.
# -> OR simply using a more restrictive range ([900,1000[)
#
# By restricting some numbers or conditions we know could never produce a
# palindrome, time would also be cut down.
#
# Easy way to reverse a number:
# a = str(number)
# reverseNumber = number[::-1]
#
# Cheats:
# https://stackoverflow.com/questions/15559490/finding-largest-palindrome-of-a-multiplication-of-2-3-digits-numbers-limitation
# Is that a cheat?
# >_>

palindromes = []
for x in range(900, 1000):
    for y in range(900, 1000):
        a = str(x * y)
        p = a[::-1] #Magics
        if a == p:
            palindromes.append(p)
            
# If there are palindromes obtained by multiplying two numers in the set
# [900, 1000[ then one of those is surely the answer.

print(max(palindromes))

###############################################################################
# Fuck lists man! Damn memory hoggers!

b = 0
for x in range(900, 1000):
    for y in range(900, 1000):
        a = str(x * y)
        p = a[::-1] #Magics
        if a == p and int(a) > int(b):
            b = a
# Just because the palindrome found is the last one, does not mean that is 
# the largest one.
# so it has to be "if a == p and a > b"  (b being the placeholder varible that 
# holds the largest number found so far)
# and not just if a == p: b = a

print(b)
