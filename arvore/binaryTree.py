from node import Node

class BinaryTree():
    def __init__(self, data):
        self.raiz = Node(data)

    def addEsq(self, data):
        point = self.raiz
        folha = Node(data)
        if point.ant == None:
            point.ant = folha
        elif point.next == None:
            point.next = folha
        else:
            while True:
                point = point.ant

