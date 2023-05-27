def custom_sort(vector:list)->list:
    """Divide and Conquer, sorted array"""
    if len(vector) <= 2:
        return vector

    else:
        mid = len(vector) // 2
        vector.insert(1, vector.pop(mid))
        i = 1
        for idx in range(2, len(vector)-1, 2):
            vector.insert(idx+1, vector.pop(mid+i))
            i +=1
        return vector

if __name__ == '__main__':
    vector = [i for i in range(1, 5)]
    print(custom_sort(vector))