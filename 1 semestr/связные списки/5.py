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

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

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

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.nref

    def scorso(self):
        if self.start_node is None:
            return
        else:
            n = self.start_node
            while n.nref is not None:
                n = n.nref
            return n
        
    def posledovatelnost(self):
        if self.start_node is None:
            print("Список пуст")
            return
        if self.start_node.nref is None:
            print(self.start_node.item)
            return
        else:
            n = self.start_node
            k = self.scorso()
            while n.item<=k.item:
                if n.item==k.item:
                    print(n.item , " ")
                else:
                    print(n.item , " ")
                    print(k.item , " ")
                n = n.nref
                k = k.pref
b = DoublyLinkedList()
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
    b.insert_at_end(a[i])
b.posledovatelnost()
