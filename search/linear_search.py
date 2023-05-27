from typing import Union
import numpy as np
from calc_time import calc_time

@calc_time
def linear_search(l:list, value:Union[int, float, str])->int:
    """ Returns the index of the value in the list if found, else returns -1"""
    try:
        for i in range(len(l)):
            if l[i] == value:
                return i
        return -1
    except Exception as e:
        print(e)
        return -1

if __name__ == "__main__":
    size = 10**8
    l = list(np.random.rand(size))
    print(linear_search(size, 0.5))