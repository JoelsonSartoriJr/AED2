import unittest

fibobacci_cache = {}
def fib_cache(x):
    """Fibonacci dynamic programming
    
    Arguments:
        x {integer} -- Index Fibonacci
    
    Returns:
        integer -- Calculate number fibonacci
    """
    if x in fibobacci_cache:
        return fibobacci_cache[x]
    
    if x <= 2:    
        value = 1

    elif x > 2:
        value = fib_cache(x-1) + fib_cache(x-2)
    
    fibobacci_cache[x] = value
    return value

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fib_cache(1), 1)
        self.assertEqual(fib_cache(2), 1)
        self.assertEqual(fib_cache(3), 2)
        self.assertEqual(fib_cache(4), 3)
        self.assertEqual(fib_cache(5), 5)
        self.assertEqual(fib_cache(6), 8)
        self.assertEqual(fib_cache(7), 13)
        self.assertEqual(fib_cache(8), 21)