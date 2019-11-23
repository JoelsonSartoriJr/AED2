def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while (j >= 0) and (A[j] > key):
            A[j+1] = A[j]
            j -= 1
        A[j + 1] = key
    return A

u = [1,2,3,4,5,6]
v = [6,5,4,3,2,1]

print(insertion_sort(u))
print(insertion_sort(v))