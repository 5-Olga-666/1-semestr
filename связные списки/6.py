#push() - добавляет элемент в стек и перемещает указатель на этот элемент стека
#pop() : возвращает "верхний" (top) элемент и перемещает указатель на 2-й элемент стека.
#top() : возвращает "верхний" (top) элемент.
#size() : возвращает размер стека.
#isEmpty() : возвращает True если стек пуст, в противном случае возвращает False.
#printstack() : выводит на экран все элементы стека
class Node(self, data):
    self.item = data
    self.nref = None
    self.pref = None
class Stack(self):
    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def top(self):
        return self.top

    def insert_in_emptylist(self, data):
        if self.isEmpty == True:
            new_node = Node(data)
            self.top = new_node
        else:
            print("list is not empty")

    def push(self, data, n):
        if self.isEmpty == True:
            new_node = Node(data)
            self.top = new_node
        else:
            new_node = Node(data)
            new_node.nref = self.start_node
            self.top.pref = new_node
            self.top = new_node
        n = self.top

    def pop(self, n):
        if self.isEmpty == True:
            print("Список пуст")
            return
        else:
            n = self.top.nref
            return self.top

    def size(self):
        if self.isEmpty == True:
            print("Список пуст")
            return
        else:
            i = 0
            n = self.top
            while n is not None:
                i = i+1
                n = n.nref
        return i

    def traverse(self):
        if self.isEmpty == True:
            print("Список пуст")
            return
        else:
            n = self.top
            while n is not None:
                print(n.item, " ")
                n = n.nref

            
            
            
