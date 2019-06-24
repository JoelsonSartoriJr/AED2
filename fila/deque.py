from node import Node

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def insertIni(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.ant = node
            self.head = node
            self.head.ant = None
        self._size += 1

    def insertEnd(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.ant = self.tail
            self.tail.next = node
            self.tail = node
        self._size +=1
    
    def removeIni(self):
        if self._size > 0:
            elem = self.head.data
            self.head = self.head.next
            self._size -= 1
            self.head.ant = None
            return elem
        raise IndexError("Deque empty!")

    def removeEnd(self):
        if self._size > 0:
            elem = self.tail.data
            self.tail = self.tail.ant
            self._size -= 1
            self.tail.next = None
            return elem
        raise IndexError("Deque empty")

    def consultIni(self):
        #retorna o topo sem remover
        if self.head != None:
            elem = self.head.data
            return elem
        else:
            print ("fila vazia.")
    
    def consultEnd(self):
        #retorna o fim sem remover
        if self.tail != None:
            elem = self.tail.data
            return elem
        else:
            print ("fila vazia.")        
    
    def destroi(self):
        self.ini = -1
        self.end = -1
        self._size = 0

    def __repr__(self):
        r = '['
        pointer = self.head
        while (pointer):
            r = r + str(pointer.data) + ','
            pointer = pointer.next
        return r + ']'

    def __str__(self):
        return self.__repr__()    
        
        

f = Deque()

f.insertIni(1)
f.insertIni(2)
f.insertIni(3)
f.insertEnd(30)
f.insertEnd(31)
print(f)
print('-----------------------')
f.removeIni()
print(f)
print('-----------------------')
f.removeEnd()
print(f)