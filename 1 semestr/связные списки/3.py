#односвязный список
#функция добавления элемента в произвольное место
#функция удаления элемента по значению
#функция выведения списка
#для текущего состояния списка вычислить последовательность элементов a[i] - a[n]
class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
class OneLinkedList:
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
            print("Node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
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
    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            k = self.start_node
            while k is not None:
                if k.item == x:
                    break
                k = k.nref
            if k is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = k.nref
                k.nref = new_node
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            if n.item == x:
                new_node = Node(data)
                new_node.nref = self.start_node
                self.start_node = new_node
            else:
                k = self.start_node.nref
                while k is not None:
                    if k.item == x:
                        break
                    n = n.nref
                    k = k.nref
                if k is None:
                    print("item not in the list")
                else:
                    new_node = Node(data)
                    n.nref = new_node
                    new_node.nref = k
    def delete(self, x):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            k = self.start_node
            n = self.start_node.nref
            while n is not None:
                if n.item == x:
                    break
                k = k.nref
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                k.nref = n.nref
    def traverse(self):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref
    def posledovatelnost(self, i):
        if self.start_node is None:
            print("Список пуст")
            return
        else:
            n = self.start_node
            k = 1
            while k!=i:
                n = n.nref
                k = k+1
            while n is not None:
                print(n.item, " ")
                n = n.nref
b = OneLinkedList()
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
    b.insert_at_end(a[i])
i = int(input())
b.posledovatelnost(i)
