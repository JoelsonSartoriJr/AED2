class Node():
    def __init__(self, data):
        self.left = None
        self.data = data
        self.bal = 0 + self.calc_bal()
        self.rigth = None

    def calc_bal(self):
        pass