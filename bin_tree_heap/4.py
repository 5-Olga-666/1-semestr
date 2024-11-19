class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def zerkalo(x,y):
    if x is None:
        y=None
    if not y is None:
        y.key=x.key
        if x.left is None and x.right is None:
            y.left=None
            y.right=None
        elif x.left is None:
            y.right=None
            zerkalo(x.right,y.left)
        elif x.right is None:
            y.left=None
            zerkalo(x.left,y.right)
        else:
            zerkalo(x.left,y.right)
            zerkalo(x.right,y.left)
d = Node(15)
e = Node(0)
d.left = Node(10)
e.left = Node(0)
d.right = Node(10)
e.right = Node(0)
d.left.left = Node(8)
e.left.left = Node(0)
d.left.right = Node(12)
e.left.right = Node(0)
d.right.left = Node(8)
e.right.left = Node(0)
d.right.left = Node(8)
e.right.left = Node(0)
zerkalo(d,e)
