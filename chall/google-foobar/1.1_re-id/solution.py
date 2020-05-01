import math

def solution(n):
    l = [2]
    last = 3
    while len(l) < n+5: # Generate at least n+5 primes
        roof = math.sqrt(last)
        for p in l:
            if p > roof:
                l.append(last)
                break
            if last % p == 0:
                break
        last += 1

    return "".join([str(a) for a in l])[n:n+5]
