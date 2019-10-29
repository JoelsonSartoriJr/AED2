class Node():
    def __init__(self, data):
        """Create Node
        
        Arguments:
            data {data} -- data reference to tree
        """
        self.left = None
        self.data = data
        self.parent = None
        self.rigth = None

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
        """Insert new data with tree
        
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
                node.left.parent = node
        else:
            if (node.rigth != None):
                self._add(data, node.rigth)
            else:
                node.rigth = Node(data)
                node.rigth.parent = node

    def remove(self, data):
        """Remove data from tree
        
        Arguments:
            data {float/integer} -- element to remove
        
        Returns:
            [bollean] -- if element contain in tree return False else return False
        """
        node = self.find(data)
        if node == False:
            print('O elemento {} não está contido na arvore.'.format(data))
            return False
        node_parent = node.parent

        #Node has no children
        if node.left == None and node.rigth == None: #Node has no children
            if node_parent.left != None and node_parent.left.data == data:
                node_parent.left = None
            else:
                node_parent.rigth = None

        #Node has children only left side
        elif node.left != None and node.rigth == None:
            if node_parent.left.data == data:
                node_parent.left = node.left
            else:
                node_parent.rigth = node.left

        #Node has children only rigth side
        elif node.rigth != None and node.left == None:
            if node_parent.left.data == data:
                node_parent.left = node.rigth
            else:
                node_parent.rigth = node.rigth

        else:
            self._remove(node, node_parent, data)
        
        print('Elemento {} removido.'.format(data))
        return True

    def _remove(self, node, node_parent, data):
        size_left = self._size_left(node.left, 0)
        size_rigth = self._size_rigth(node.rigth, 0)
        if size_left[0] > size_rigth[0]:
            old_parent = size_left[1].parent
            size_left[1].parent = node_parent
            size_left[1].left = node.left
            size_left[1].rigth = node.rigth
            if node_parent.left.data == node.data:
                node_parent.left = size_left[1]
            else:
                node_parent.rigth = size_left[1]

            if old_parent.left != None and old_parent.left.data == size_left[1].data:
                old_parent.left = None
            else:
                old_parent.rigth = None
        else:
            old_parent = size_rigth[1].parent
            size_rigth[1].parent = node_parent
            size_rigth[1].left = node.left
            size_rigth[1].rigth = node.rigth
            if node_parent.left.data == node.data:
                node_parent.left = size_rigth[1]
            else:
                node_parent.rigth = size_rigth[1]

            if old_parent.left != None and old_parent.left.data == size_rigth[1].data:
                old_parent.left = None
            else:
                old_parent.rigth = None

    def _size_left(self, node, qnt):
        if node.rigth != None:
            return self._size_left(node.rigth, qnt+1)
        else:
            return qnt, node

    def _size_rigth(self, node, qnt):
        if node.left != None:
            return self._size_rigth(node.left, qnt+1)
        else:
            return qnt, node

    def find(self, data):
        """Find data in tree
        
        Arguments:
            data {float} -- Value to be searched
        
        Returns:
            [node / boolean] -- node or False
        """
        if (self.root != None):
            return self._find(data, self.root)
        else:
            return False
    
    def _find(self, data, node):
        if data == node.data:
            return node
        elif data < node.data and node.left != None:
            return self._find(data, node.left)
        elif data > node.data and node.rigth != None:
            return self._find(data, node.rigth)
        else:
            return False

    def heigth(self):
        if self.root != None:
            return self._heigth(self.root, 0)
        else:
            return 0
    
    def _heigth(self, node, node_heigth):
        if node == None:
            return node_heigth
        left_heigth = self._heigth(node.left, node_heigth + 1)
        rigth_heigth = self._heigth(node.rigth, node_heigth + 1)
        return max(left_heigth, rigth_heigth)

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
a.add(20)
a.add(10)
a.add(30)
a.add(5)
a.add(15)
a.add(25)
a.add(35)
a.add(2)
a.add(7)
a.add(12)
a.add(18)
a.add(22)
a.add(27)
a.add(28)
a.add(32)
a.add(37)
a.printTree()
print('---{}---'.format(a.heigth()))
a.remove(30)
a.printTree()
