from Node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size += 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem):
        """Return index element in list"""
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError("{} is not in list".format(elem))

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1


lista = LinkedList()
lista.append(7)
lista.append(80)
lista.append(56)
lista.append(32)
lista.append(17)
lista.insert(0, 22)
print(lista[0])
lista.insert(3, 888)
print(lista[3])
