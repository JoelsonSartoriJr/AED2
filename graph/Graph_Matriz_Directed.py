# -*- coding: utf-8 -*-

class Graph_Matriz():

    def __init__(self, v):
        self.v = v
        self.matriz_adj = [[0] * v for _ in range(v)]
        #self.visit = [0]*v

    def insert(self, v_init, v_end, data=1):
        v_init -= 1
        v_end -= 1
        if self.matriz_adj[v_init][v_end] != 0:
            print('Vertice já existente')
            return False
        else:
            self.matriz_adj[v_init][v_end] = data
    
    def remove(self, v_init, v_end):
        v_init -= 1
        v_end -= 1
        if self.matriz_adj[v_init][v_end] != 0:
            self.matriz_adj[v_init][v_end] = 0
        else:
            print('Vertice inesistente')
            return False

    def equals(self, graph):
        if self.v == graph.v:
            for i in range(self.v):
                for j in range(self.v):
                    if self.matriz_adj[i][j] != graph.matriz_adj[i][j]:
                        print("Grafos diferentes!")
                        return False
            print("Grafos iguais!")
            return True
        else:
            print('Grafos diferentes!')
            return False

    def isolated_vertice(self, vertice):
        for i in range(self.v):
            if (self.matriz_adj[vertice][i] != None) or (self.matriz_adj[i][vertice] != None):
                print("Vertice tem conexão")
                return False
        print("Vertice não tem conexão")
        return True

    def __str__(self):
        return '\n'.join('|'.join(map(str, row)) for row in self.matriz_adj)

c1 = Graph_Matriz(5)
c1.insert(1,2)
c1.insert(2,2)
print(c1)
c1.remove(1,2)
print('Apos o remove')
print(c1)

print('----------C2------')
c2 = Graph_Matriz(5)
c2.insert(1,2)
c2.insert(2,2)
c2.insert(2,3)
print(c2)
c2.remove(1,2)
print('Apos o remove')
print(c2)
print('Verifica igualdade')
c1.equals(c2)