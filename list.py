class lista:

    def __init__(self, maxm):
        self.elemento = [0]*maxm
        self.ini = -1
        self.fim = -1
        self.maxm = maxm

    def consultar(self, pos):
        if pos > (self.fim - self.ini) or pos < self.ini:
            return False
        else:
            return self.elemento[self.ini+pos]

    def insere(self, nodo, pos):
         #Posicao maior que o espaco alocado
         #Posicao maior que o espaco alocado
         #Posicao menor do que o inicio
        if (self.ini == 0 and self.fim == self.maxm-1) or (pos > (self.fim - self.ini +1)) or  (pos < 0 or ( self.ini == -1 and pos !=0 )): 
            print("Error: posicao invalida")
        
        else:
            if self.ini == -1: #Lista vazia
                self.ini = 0
                self.fim = 0
            else:
                if self.fim != self.maxm -1:
                    for i in range(self.fim, self.ini+ pos-1, -1):
                        self.elemento[i+1] = self.elemento[i]
                    self.fim = self.fim + 1
                else:
                    for i in range(self.ini, self.ini +pos):
                        self.elemento[i-1] = self.elemento[i]
                    self.ini = self.ini-1
            self.elemento[self.ini+pos] = nodo

    def remover(self, pos):
        if pos < 0 or pos > (self.fim-self.ini):
            return "Error: Impossivel apagar lista vazia"
        else:
            rem = self.elemento[self.ini+pos]
            for i in range(self.ini+pos, self.fim):
                self.elemento[i] = self.elemento[i+1]
            self.elemento[self.fim]=0
            self.fim=self.fim-1
            return rem


def main():
    l = lista(10)
    print(l.consultar(2))
    print(l.insere('moto', 0))
    print(l.insere('carro', 1))
    print(l.insere('caminhao', 5))
    print(l.elemento)
    print(l.insere('aviao', 0))
    print(l.elemento)
    print(l.remover(1))
    print(l.elemento)
main()

