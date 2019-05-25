from Node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head: #Insercao quando a lista nao esta vazia 
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            #Insercao primeiro elemento
            self.head = Node(elem)

        self._size += 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def __getitem__(self, index):
        #Funciona a = lista[1]
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        #funciona lista[1] = 2
        pointer = self._getNode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem):
        """Retorna o indece do elemento na lista"""
        pointer = self.head
        i = 0
        while (pointer):
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
            pointer = self._getNode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    def remove(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while (pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = ancestor.next
                pointer = pointer.next
            return True
        raise ValueError("{} is not in list".format(elem))

    def __repr__(self):
        r = "["
        pointer = self.head
        while (pointer):
            r += str(pointer.data) + ","
            pointer = pointer.next
        return r + "]"

    def __str__(self):
        return self.__repr__()
        
    def compara(self, lista):
        pointer = self.head
        pointer2 = lista.head

        if self._size != len(lista):
            return False

        while (pointer):
            if pointer.data != pointer2.data:
                return False
            pointer = pointer.next
            pointer2 = pointer2.next
        return True

    def reverse(self):
        prev = None
        current = self.head

        while (current):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
        return self.__repr__()

    def maiorMedia(self):
        pointer = self.head
        med = 0
        r = ''
        while (pointer):
            med += pointer.data
            pointer = pointer.next
        med = med / self._size
        pointer = self.head
        cont = 0
        while (pointer):
            if pointer.data > med:
                r += "({},{})".format(pointer.data, cont)
            pointer = pointer.next
            cont += 1
        return r