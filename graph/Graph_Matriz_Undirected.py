# -*- coding: utf-8 -*-


class Graph_Matriz_Undirected():

    def __init__(self, v):
        self.v = v
        self.matriz_adj = [[0] * v for _ in range(v)]

    def insert(self, v_init, v_end, data=1):
        v_init -= 1
        v_end -= 1
        if self.matriz_adj[v_init][v_end] != 0:
            print('Vertice já existente')
            return False
        else:
            self.matriz_adj[v_init][v_end] = data
            self.matriz_adj[v_end][v_init] = data
    
    def remove(self, v_init, v_end):
        v_init -= 1
        v_end -= 1
        if self.matriz_adj[v_init][v_end] != 0:
            self.matriz_adj[v_init][v_end] = 0
            self.matriz_adj[v_end][v_init] = 0
        else:
            print('Vertice inesistente')
            return False

    def __str__(self):
        return '\n'.join('|'.join(map(str, row)) for row in self.matriz_adj)

c = Graph_Matriz_Undirected(5)
c.insert(1,2)
c.insert(2,2)
print(c)
c.remove(1,2)
print('Apos o remove')
print(c)