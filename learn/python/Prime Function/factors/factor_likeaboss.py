def prime(n):
	i = 2
	
	while i**2 < n:
		while n % i == 0:
			n = n // i
		i += 1
	
	return n

if __name__ == "__main__":
	print(prime(600851475143))
