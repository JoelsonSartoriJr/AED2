class lista:
    def __init__(self, maxx):
        self.maxx = maxx
        self.elemento = [0] * maxx
        self.ini = -1
        self.fim = -1
    
    def consulta(self, pos):
        if pos > self.fim or pos < 0:
            raise IndexError("Posição não se encontra na lista!")
        return self.elemento[self.ini + pos]
        
    def insere(self, elem, pos):
        if (self.ini == 0 and self.fim == self.maxx - 1) or (pos > self.fim - self.ini + 1) or (pos < 0) or (self.ini == -1 and pos != 0):
            raise IndexError("Posição invalida")
            
        else:
            if self.ini == -1:
                self.ini = 0
                self.fim = 0
            else:
                if self.fim != self.maxx - 1:
                    for i in range(self.fim, self.ini + pos - 1, -1):
                        self.elemento[i + 1] = self.elemento[i]
                    self.fim = self.fim + 1
                else:
                    for i in range(self.ini, self.ini + pos):
                        self.elemento[i - 1] = self.elemento[i]
                    self.ini = self.ini-1  
            self.elemento[self.ini + pos] = elem
            return print("Elemento {} inserido".format(elem))

    def remover(self, pos):
        if (pos > self.fim - self.ini) or pos < 0:
            raise IndexError("Posição invalida")
        else:
            rem = self.elemento[self.ini + pos]
            if (pos - self.ini > self.fim - pos):
                for i in range(self.ini + pos, self.fim):
                    self.elemento[i] = self.elemento[i + 1]
                self.elemento[self.fim] = 0
                self.fim -= 1
            else:
                for i in range(self.ini + pos, self.ini, -1):
                    self.elemento[i] = self.elemento[i - 1]
                self.elemento[self.ini] = 0
                self.ini += 1
            return print("Elemento {} removido".format(rem))
    def destroi(self):
        self.elemento = None
        self.ini = -1
        self.fim = -1

l = lista(5)
l.insere("carro", 0)
l.insere("moto", 1)
l.insere("Bicicleta", 2)
print(l.elemento)
l.remover(2)
print(l.elemento)
l.insere("Bicicleta", 2)
#l.insere("Caminhao", 9)
l.insere("Caminhao", 3)
print(l.elemento)
l.insere(l.consulta(1), 0)
print(l.elemento)
