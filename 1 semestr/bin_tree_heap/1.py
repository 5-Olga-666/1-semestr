class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def simmetria(x,y):
    if x is None and y is None:
        return True
    return (x is not None and y is not None) and (x.key==y.key) and simmetria(x.left,y.right) and simmetria(x.right,y.left)
d = Node(15)
d.left = Node(10)
d.right = Node(10)
d.left.left = Node(8)
d.left.right = Node(12)
d.right.left = Node(8)
d.right.left = Node(8)
if simmetria(d,d):
    print("Дерево симметричное")
else:
    print("Дерево несимметричное")
