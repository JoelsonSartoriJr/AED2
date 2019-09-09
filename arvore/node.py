class Node():
    def __init__(self, data):
        """Create Node
        
        Arguments:
            data {data} -- data reference to tree
        """
        self.data = data
        self.next = None
        self.ant = None