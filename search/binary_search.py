from typing import Union
from calc_time import calc_time
import numpy as np

@calc_time
def binary_search(vector:list, value:Union[int, float, str])->int:
    """binary search in an ordered vector"""
    try:
        l = len(vector)
        if l >= 1:
            mid = l//2
            if vector[mid]==value:
                return 1
            elif vector[mid]>value:
                return binary_search(vector[:mid], value)
            elif vector[mid]<value:
                return binary_search(vector[mid+1:], value)
        else:
            return -1
    
    except Exception as e:
        print(e)
        return -1
    
if __name__ == "__main__":
    size = 10**7
    vector = list(np.random.rand(size))
    print(binary_search(vector, 0.5))
