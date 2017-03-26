from math import sqrt

def isprime(n):
    if n == 2:
        return True
    
    if n < 2:
        return False
        
    for x in range(2, int(sqrt(n))+1, 1):
        if n % x == 0:
            return False
            
    return True

run = True
while run:
	try:
		x = int(input("Input a number to check if it's prime. Type 'exit' to quit.\n>>> "))
		print(isprime(x))
	except Exception:
		run = False


# Usability options
""""
while 1:
    n = input("Please enter a whole number:")
    try:
        n = int(n)
        print(prime(n))
    except ValueError:
        print("Please enter a whole number - a positive integer.")
"""
