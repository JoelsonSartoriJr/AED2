from node import Node

class pilha:
    def __init__(self,):
        self.top = None
        self._size = 0
        
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self._size += 1
        
    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        raise IndexError("List empty")

    def peek(self):
        if self._size > 0:
            return self.top.data
        raise IndexError("A pilha está vazia")

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ''
        pointer = self.top
        while (pointer):
            r += str(pointer.data) +'\n'
            pointer = pointer.next
        return r

p = pilha()
p.push(1)
p.push(2)
p.push(3)
p.push(4)
p.push(5)
print(p.peek())