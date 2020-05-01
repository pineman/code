def get_parent(n, h, parent):
    #print "called with", n, h, parent
    if parent == -1:
        subroot = 2**h-1
    else:
        subroot = parent
    right = subroot - 1
    left = right - 2**(h-1)+1
    #print subroot, right, left

    if n == subroot:
        #print "returned", parent
        return parent

    if n == right or n == left:
        #print "returned", subroot
        return subroot

    if n < left:
        # go left subtree
        #print "went left"
        return get_parent(n, h-1, left)
    else:
        # go right subtree
        #print "went right"
        return get_parent(n, h-1, right)

def solution(h, q):
    # 1 <= h <= 30
    # lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.
    p = []
    for n in q:
        p.append(get_parent(n, h, -1))
    return p


#print solution(3, [7, 3, 5, 1])
#print solution(3, [7, 3, 5, 1]) == [-1, 7, 6, 3]
#print solution(5, [19, 14, 28])
#print solution(5, [19, 14, 28]) == [21, 15, 29]
