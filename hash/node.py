class Node():
    def __init__(self, key, data):
        """Create a new node
        
        Arguments:
            key {[type]} -- [description]
            data {[type]} -- [description]
        """
        self.key = key
        self.data = data
        self.next = None