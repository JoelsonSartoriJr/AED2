

def fib_low(x):
    """[summary]
    
    Arguments:
        x {integer} -- Index Fibonacci
    
    Returns:
        Integer -- Calculate number fibonacci
    """
    if x<= 2:
        return 1
    else:
        return fib_low(x-1) + fib_low(x-2)


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
