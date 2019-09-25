fibobacci_cache = {}

def fib(x):
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
        value = fib(x-1) + fib(x-2)
    
    fibobacci_cache[x] = value
    return value

print(fib(2))