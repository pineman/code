def fizzbuzz(n):
    out = ""
    if n % 3 == 0:
        out += "Fizz"
    if n % 5 == 0:
        out += "Buzz"
    if not out:
        out = str(n)
    return out

def fizzbuzz_r(n):
    divThree = n % 3 == 0
    divFive = n % 5 == 0
    if divThree and DivFive:
        return "FizzBuzz"
    if divThree:
        return "Fizz"
    if divFive:
        return "Buzz"
    return str(n)

def fizzbuzz_of_the_christ(n):
    return "FizzBuzz"[i*i%3*4:8--i**4%5] or i

for n in range(1, 101):
    #print(fizzbuzz(n))
    #print(fizzbuzz_r(n))
    print(fizzbuzz_of_the_christ(n))

