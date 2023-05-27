from typing import Union
from calc_time import calc_time
import numpy as np

@calc_time
def sentinel_search(vector:list, value:Union[int, float, str])->int:
    """ Returns the index of the value in the list if found, else returns -1"""
    try:
        vector.append(value)
        i = 0
        while vector[i] != value:
            i += 1
        if i == len(vector) - 1:
            return -1
        return i
    except Exception as e:
        print(e)
        return -1
    
if __name__ == "__main__":
    size = 10**7
    vector = list(np.random.rand(size))
    print(sentinel_search(vector, 0.5))