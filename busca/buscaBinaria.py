def binarySearch(v,n):
    """binary search in an ordered vector
    
    Arguments:
        v {vector} -- vector with ordered elements
        n {integer} -- search number
    
    Returns:
        boolean -- true if element exist in list
    """
    l = len(v)
    if l >= 1:
        mid = l//2
        if v[mid]==n:
            return True
        elif v[mid]>n:
            return binarySearch(v[:mid],n)
        elif v[mid]<n:
            return binarySearch(v[mid+1:],n)
    else:
        return False

def binary_Search(v, start = 0, end = len(v), n):
    """binary search in an ordered vector
    
    Arguments:
        v {vector} -- vector with ordered elements
        start {integer} -- init vector
        end {integer} -- end vector
        n {integer} -- search number
    
    Returns:
        [integer or boolean] -- integer if element exist in vector
    """
    if not start < end:
        return False
    mid = (start+end)//2
    if v[mid] > n:
        return binary_Search(v, start, mid, n)
    elif v[mid]<n:
        return binary_Search(v, mid+1, end, n)
    else:
        return mid

        
v = [1,3,4,5,7]
print(binary_Search(v, 0, len(v),5))
