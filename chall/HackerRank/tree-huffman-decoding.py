"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    #Enter Your Code Here
    def isLeaf(t):
        return t.left == None and t.right == None
    r = ''
    t = root
    for c in s:
        if c == '1':
            t = t.right
        else:
            t = t.left
        if isLeaf(t):
            r += t.data
            t = root
    print(r)

