from node import Node

class Hash():
    def __init__(self, size):
        """init class
        
        Arguments:
            size {integer} -- hash table size
        """
        self._size = size
        self._newSize = self.primo()
        self._vector = [0]*(self._newSize)

    def primo(self):
        """Computer next prime number
        
        Returns:
            [integer] -- number
        """
        primo = self._size + self._size//2 + 1
        while True:
            if primo%2 == 0 or primo%3 == 0 or primo%5 == 0 or primo%7 == 0:
                primo +=1
            else:
                return primo

    def hashing(self, newNode):
        """Computer the position for the new node
        
        Arguments:
            newNode {Node} -- Linked list
        
        Returns:
            inteter -- number
        """
        return newNode.key%self._newSize
    
    def add(self, data):
        """Add new data to hash table
        
        Arguments:
            data {Node} -- Linked list
        
        Returns:
            [inter] -- Hash table position
        """
        newNode = Node(data[0], data[1])
        pos = self.hashing(newNode)
        if self._vector[pos] != 0:
            point = self._vector[pos]
            while point.next:
                point = point.next
            point.next = newNode
        else:
            self._vector[pos] = newNode
        return pos


