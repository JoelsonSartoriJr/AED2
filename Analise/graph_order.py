
import numpy as np
import matplotlib.pyplot as plt



n = [i for i in range(1, 100000)]
colors = ['#8B4513', '#FF4500', '#87CEEB', '#008080']
#Cost for a sorted array
o_insert_sort = n
o_buble_sort = n
o_merge_sort = [i*np.log(i) for i in n]
o_quick_sort = [i*np.log(i) for i in n]

fig, ax = plt.subplots()
ax.plot(n, o_insert_sort, label='Insertion Sort', color=colors[0])
ax.plot(n, o_buble_sort, label='Buble Sort', color=colors[1])
ax.plot(n, o_merge_sort, label='Merge Sort', color=colors[2])
ax.plot(n, o_quick_sort, label='Quick Sort', color=colors[3])
ax.set_xlabel('Tamanho do vetor')
ax.set_ylabel('Tempo de execução')
ax.set_title('Tempo de execução para vetores ordenados')
ax.legend()
plt.savefig('graph_order.png')

#Cost for a reverse-sorted array
i_insert_sort = [i**2 for i in n]
i_buble_sort = [i**2 for i in n]
i_merge_sort = [i*np.log(i) for i in n]
i_quick_sort = [i**2 for i in n]

fig, ax = plt.subplots()
ax.plot(n, i_insert_sort, label='Insertion Sort', color=colors[0])
ax.plot(n, i_buble_sort, label='Buble Sort', color=colors[1])
ax.plot(n, i_merge_sort, label='Merge Sort', color=colors[2])
ax.plot(n, i_quick_sort, label='Quick Sort', color=colors[3])
ax.set_xlabel('Tamanho do vetor')
ax.set_ylabel('Tempo de execução')
ax.set_title('Tempo de execução para vetores inversamnete ordenados')
ax.legend()
plt.savefig('graph_inverse_order.png')

#Cost for an unordered vector.
insert_sort = [i**2 for i in n]
buble_sort = [i**2 for i in n]
merge_sort = [i*np.log(i) for i in n]
quick_sort = [i*np.log(i) for i in n]

fig, ax = plt.subplots()
ax.plot(n, insert_sort, label='Insertion Sort', color=colors[0])
ax.plot(n, buble_sort, label='Buble Sort', color=colors[1])
ax.plot(n, merge_sort, label='Merge Sort', color=colors[2])
ax.plot(n, quick_sort, label='Quick Sort', color=colors[3])
ax.set_xlabel('Tamanho do vetor')
ax.set_ylabel('Tempo de execução')
ax.set_title('Tempo de execução para vetores inversamnete ordenados')
ax.legend()
plt.savefig('graph.png')