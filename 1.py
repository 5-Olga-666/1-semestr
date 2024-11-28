class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
        
    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def find_in_list(self, x):
        if self.start_node is None:
            print("false")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    print("true")
                    break
                n = n.nref
            if n is None:
                print("false")

b = DoublyLinkedList()
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
    b.insert_at_end(a[i])
y = int(input())
b.find_in_list(y)
