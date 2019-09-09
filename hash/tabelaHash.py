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
            integer -- number
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
            integer -- number
        """
        return newNode.key%self._newSize
    
    def add(self, data):
        """Add new data to hash table
        
        Arguments:
            data {Node} -- Linked list
        
        Returns:
            integer -- Hash table position
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

    def search(self, data):
        """Search data in hash table
        
        Arguments:
            data {Node} -- Linked list
        
        Returns:
            boolean -- True or False
        """
        searchNode = Node(data[0], data[1])
        pos = self.hashing(searchNode)
        if self._vector[pos] != 0 and self._vector[pos].data == searchNode.data:
            print("({}:{})".format(self._vector[pos].key, self._vector[pos].data))
            return True
        elif self._vector[pos] != 0 and self._vector[pos].next != None:
            point = self._vector[pos]
            while point.next:
                point = point.next
                if point.data == searchNode.data:
                    print("({}:{})".format(point.key, point.data))
                    return True
            print("Dado não encontrado")
            return False
        else:
            print("Dado não encontrado")
            return False

    def __del__(self):
        """
            Destruct Hash table
        """
        print("Tabela Hash destruida")


a = Hash(10)
a.add([73,"joão"])
a.search([73,"Maria"])
a.add([73,"Maria"])
a.search([73,"Maria"])