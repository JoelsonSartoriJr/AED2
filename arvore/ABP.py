from node import Node

class BinaryTree():
    """Create a Binary Tree
    
    Returns:
        Object -- Binary Tree
    """
    def __init__(self):
        """Init Binary tree
        """
        self.root = None
        print('Arvore criada')

    def add(self, data):
        """Add elem in Tree
        
        Arguments:
            data {float/integer} -- Value to add in tree
        """
        if self.root == None:
            self.root = Node(data)
        else:
            self._add(data, self.root)
    
    def _add(self, data, node):
        if data < node.data:
            if (node.left != None):
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if (node.rigth != None):
                self._add(data, node.rigth)
            else:
                node.rigth = Node(data)

    def find(self, data):
        """Find value in tree
        
        Arguments:
            data {float} -- Value to be searched
        
        Returns:
            [boolean] -- True if the element contains in the tree else false 
        """
        if (self.root != None):
            return self._find(data, self.root)
        else:
            return False
    
    def _find(self, data, node):
        if data == node.data:
            return True
        elif data < node.data and node.left != None:
            return _find(data, node.left)
        elif data > node.data and node.rigth != None:
            return _find(data, node.rigth)
    
    def printTree(self):
        """Print Binary tree
        """
        if (self.root != None):
            self._printTree(self.root)
    
    def _printTree(self, node):
        if (node != None):
            self._printTree(node.left)
            print('{} '.format(node.data))
            self._printTree(node.rigth)

    def deleteTree(self):
        self.root = None
            
a = BinaryTree()
a.add(10)
a.add(9)
a.add(11)
a.add(12)
a.add(8)
a.printTree()