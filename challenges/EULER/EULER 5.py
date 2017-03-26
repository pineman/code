"""
EULER 5
http://projecteuler.net/problem=5
------------------------------------
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
# I'll calculate the Least Common Multiple (LCM) by this method:
# https://en.wikipedia.org/wiki/Least_common_multiple#Finding_least_common_multiples_by_prime_factorization
#
# Firstly, find the prime factors of the numbers [1, 20]

primes = [2, 3, 5, 7, 11, 13, 17, 19]
max_factors = {}
default = 0
for p in primes:
    max_factors.setdefault(p, default)
# Have to set values for the dictionary's keys (in this case, the keys will be 
# each prime) 
# in order to compare in line 46, otherwise this will happen:
# https://wiki.python.org/moin/KeyError
#
# Working factorization
for n in range(4, 21):
    # Initialize factorization
    b = n
    if b not in primes:
        factors = []
        while b > 1:
            for x in primes:
                if int(b) % x != 0:
                    continue
                else:
                    factors.append(x)
                    b = int(b/x)
    else:
        factors = []
        factors.append(n)
    # Factorization's over for iteration n

# At this point, I've got a (temporary) list of factors for each number.
# Now, append the value of (highest count of factor f)
# to the key [f] of the dictionary " max_factors "
# notice the indentation.

    for f in primes:
        a = (factors.count(f))
        # The variable "a" is the number of occurrences of a 
        # given factor "f".
        # Therefore, it's "f"'s exponent.
        if a > max_factors[f]:
            max_factors[f] = a
 
# print(max_factors)
# OMG!!! IT WORKS!!!!

# "The lcm will be the product of multiplying the highest power of each prime
#  number together."
# 
# Now that I've got all the highest powers of each factor in a handy dandy
# dictionary, all there's left to do is find a way to multiply all
# ( factor^(ocurrences of factor) )

pairs = max_factors.items()

factor_tothepowerof_occurrence = [fac ** occ for fac, occ in pairs]

product = 1
for number in factor_tothepowerof_occurrence:
        product *= number
        
print(product)
# GGGGGGGGGGGGGGGGGGGGGGGGGG
# https://www.youtube.com/watch?v=5es0NNtSNCU

###############################################################################
# Cool .replace stuff
"""
            factors_str = str(factors)
            formatted_factors = factors_str.replace(" ","")
            formatted_factors = formatted_factors.replace("[", "").replace("]", "")
            formatted_factors = formatted_factors.replace(","," x ")
            print(formatted_factors)        
            print() 
        else:
            print(str(n) + " is a prime number already!")
            print()
"""