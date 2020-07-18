#!/usr/bin/env python3

from gmpy2 import is_prime


def prime():
    primes = [x for x in range (3, 2000000, 2) if is_prime(x)]
    totalsum = sum(primes) + 2
    return "The total sum is:\n" + str(totalsum)


if __name__ == "__main__":
	print(prime())
