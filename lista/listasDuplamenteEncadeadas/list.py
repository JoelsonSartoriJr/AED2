from Node import Node

class list():
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, data):

        if self.head: #Insercao quando a lista nao esta vazia 
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(data, pointer)
        else:
            #Insercao primeiro elemento
            self.head = Node(data)

        self._size += 1

    def __len__(self):
        return self._size

    def insert(self, data, pos):
        if pos > self._size or pos < 0:
            raise IndexError("list index out of range")
        elif pos == 0:
            self.head = Node(data, None, self.head)
            if (self.head.next != None):
                self.head.next.ant = self.head
        else:
            pointer = self.head
            for i in range(1, pos):
                pointer = pointer.next
            pointer.next = Node(data, pointer, pointer.next)
            pointer.next.ant = pointer
        self._size += 1

    def remove(self, pos):
        data = 0
        if pos > self._size or pos < 0:
            raise IndexError("list index out of range")
        elif pos == 0:
            data = self.head.data
            self.head = self.head.next
        self._size -= 1
        return data

    def posRevers(self, data):
        pointer = self.head
        while (pointer.next):
            pointer = pointer.next
        i = -1
        while (pointer.ant):
            if pointer.data == data:
                return i
            pointer = pointer.ant
            i -= 1
        raise ValueError("{} is not in list".format(data))
        
    def dataRevers(self, pos):
        if pos < 0 or pos > self._size:
            raise IndexError("list index out of range")
        else:
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            for i in range(1,pos):
                pointer = pointer.ant
            return pointer.data

    def __str__(self):
        if (self.head):
            r = "["
            pointer = self.head
            while (pointer.next):
                r += str(pointer.data) + ','
                pointer = pointer.next
            r += str(pointer.data) + "]" 
            return r
        else:
            return "[]"

    def destroi(self):
        self.head = None

    
l = list()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.insert(100, 2)
print(len(l))
print(l)
l.remove(0)
print(l)
print(len(l))
print(l.posRevers(5))
print(l.dataRevers(2))
l.destroi()
print(l)