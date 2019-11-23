def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        smallest = i
        for j in range(i+1, n):
            if (A[j] < A[smallest]):
                    smallest = j
        A[i], A[smallest] = A[smallest], A[i]

    return A
    
u = [1,2,3,4,5,6]
v = [6,5,4,3,2,1]

print(selection_sort(u))
print(selection_sort(v))