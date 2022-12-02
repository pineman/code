with open('input') as f:
    t = 0
    s = []
    for l in f:
        if l == '\n':
            s.append(t)
            t = 0
        else:
            t += int(l)
    s = sorted(s)
    print(s[-1])
    print(sum(s[-3:]))

