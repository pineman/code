a = [1,2,[3,4,[5,6]],7,[8],9]
b = []
c = [1]

def flatten(l):
    n = []
    for e in l:
        if isinstance(e, list):
            n += flatten(e)
        else:
            n.append(e)
    return n

print(flatten(a) == [1,2,3,4,5,6,7,8,9])
print(flatten(b) == [])
print(flatten(c) == [1])
