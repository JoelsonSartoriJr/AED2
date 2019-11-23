def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

u = [1,2,3,4,5,6]
v = [6,5,4,3,2,1]

print(bubble_sort(u))
print(bubble_sort(v))