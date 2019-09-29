import unittest

def fib(n):
    """Calculate fibonacci
    
    Arguments:
        n {integer} -- Index Fibonacci
    
    Returns:
        integer -- Calculate number fibonacci
    """
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(8), 21)
