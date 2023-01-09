a = [1,23,56,6,23,6,7,34,6,234]

def bs_r(l, e, start, end):
    if start > end:
        if e == l[start]:
            return start
        return None
    m = (start + end) // 2
    if e > l[m]:
        return bs_r(l, e, m+1, end)
    elif e < l[m]:
        return bs_r(l, e, start, m-1)
    else:
        return m
    

def bs_i(l, e):
    start, end = 0, len(l)-1
    while start <= end:
        mid = (start+end)//2
        if e > l[mid]:
            start = mid + 1
        elif e < l[mid]:
            end = mid - 1
        else:
            return mid
    return None

a.sort()
print(a)
print(bs_r(a, 234, 0, len(a)-1))
print(bs_i(a, 234))
print(bs_r(a, 9, 0, len(a)-1))
print(bs_i(a, 9))
