"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    def r(t):
        s = ''
        s += f'{t.info} '
        if t.left:
            s += r(t.left)
        if t.right:
            s += r(t.right)
        return s
    print(r(root))

