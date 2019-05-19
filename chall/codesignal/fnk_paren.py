import math

def revip(s, i, j):
    print(s[i:j])
    for x in range(math.ceil((j+i)/2)-i):
        s[x+i], s[j-x-1] = s[j-x-1], s[x+i]
    print(s[i:j])

a = 'th(equic)kbrown'
cr = 2
nl = 8
print(a[cr+1:nl])
revip(list(a), cr+1, nl)
print(a)
