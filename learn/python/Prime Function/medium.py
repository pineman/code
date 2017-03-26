#!/usr/bin/env python3

def prime():
	primos = [2]

	for num in range(3, 2000000, 2):
	# We want to add all the prime numbers, so remove even ones, using step = 2
		roof = num**(0.5)
		for prime in primos:
		# Now we only divide by the prime numbers we already know.
			if prime > roof:
				primos.append(num)
				break
		# If number isn't prime... break.
			if num % prime == 0:
				break

	return "The total sum is:\n" + str(sum(primos))

if __name__ == "__main__":
	print(prime())
