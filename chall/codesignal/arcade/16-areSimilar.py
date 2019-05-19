def areSimilar(a, b):
    if a == b:
        return True

    da = {}
    db = {}
    for c in a:
        da[c] = da.get(c, 0) + 1
    for c in b:
        db[c] = db.get(c, 0) + 1
    if da != db:
        return False

    comp = [0]*len(a)
    for i in range(len(a)):
        if a[i] == b[i]:
            comp[i] = 1

    print(comp)

    return comp.count(0) == 2

# too dumb for this one
"""
from collections import Counter as C

def areSimilar(A, B):
    return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3
"""
