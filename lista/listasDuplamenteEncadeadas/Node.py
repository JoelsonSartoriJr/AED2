class Node:
    def __init__(self, data, ant=None, next = None):
        self.data = data
        self.next = next
        self.ant = ant