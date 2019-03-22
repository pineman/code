def prime():
	totalsum = 2

	for num in range(3, 2000000, 2):
	# step = 2 skips even numbers
	# Tests against being prime, instead of testing for being prime.
		isPrime = True
		for n in range(3, int(num ** 0.5 ) + 1, 2 ):
		# Tests for all numbers j in the set
		# [3, sqrt(num)]
			if num % n == 0:
				isPrime = False
				break

		if isPrime:
			totalsum = totalsum + num

	return "The total sum is:\n" + str(totalsum)

if __name__ == "__main__":
	print(prime())
