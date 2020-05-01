def base10_to_b(s, b):
    r = []
    while s:
        r.append(s % b)
        s //= b
    return ''.join(str(a) for a in r[::-1]) or '0'


def step(n, b):
    x = int(''.join(sorted(n))[::-1], b)
    y = int(''.join(sorted(n)), b)
    z = base10_to_b(x - y, b)
    z = z.zfill(len(n))
    return z


def solution(n, b):
    # 2 <= len(n) <= 9 and 2 <= b <= 10
    #r = [n]
    r = {}
    c = None
    while True:
        n = step(n, b)
        r[n] = r.get(n, 0) + 1
        #c = __import__('collections')__.Counter(r)
        #if 3 in c.values()
        if 3 in r.values():
            break

    #return len([d for d in c.values() if d > 1])
    return len([d for d in r.values() if d > 1])


print solution('210022', 3) == 3
print solution('1211', 10) == 1
