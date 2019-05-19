def commonCharacterCount(s1, s2):
    #return sum([min(s1.count(c),s2.count(c)) for c in set(s1) & set(s2)])
    d1 = {}
    d2 = {}
    for c in s1:
        d1[c] = d1.get(c, 0) + 1
    for c in s2:
        d2[c] = d2.get(c, 0) + 1

    t = 0
    for i in range(ord('a'), ord('z')+1):
        t += min(d1.get(chr(i), 0), d2.get(chr(i), 0))

    return t
