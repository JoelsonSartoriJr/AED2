class Descritor:

    def __init__(self, init=-1, init_list=-1, min_element=-1, max_element=-1,
                 maxm=-1, leng=-1, fim=-1, fim_list=-1):
        self.init = init
        self.init_list = init_list
        self.min_element = min_element
        self.max_element = max_element
        self.maxm = maxm
        self.leng = leng
        self.fim = fim
        self.fim_list = fim_list


class lista:

    def __init__(self, maxm):
        self.elemento = [0]*maxm
        self.descritor = Descritor(init=-1, fim=-1,)

    def consultaElement(self, element):
        for i in range(self.descritor.init, self.descritor.fim+1):
            if self.elemento[i] == element:
                return i
        return -1

    def consultar(self, pos):
        if pos > (self.descritor.leng or pos < self.descritor.init):
            return False
        else:
            return self.elemento[self.descritor.init+pos]

    def insereExp(self, n1, n2):
        index = self.consultaElement(n1)
        if index == -1:
            print("Valor não consta na lista")
            return -1
        self.insere(n2, index)

    def insere(self, nodo, pos):
         # Posicao maior que o espaco alocado
         # Posicao maior que o espaco alocado
         # Posicao menor do que o inicio
        if (self.descritor.init == 0 and self.descritor.fim == self.descritor.maxm-1) or (pos > (self.descritor.fim - self.descritor.fim + 1)) or (pos < 0 or (self.descritor.init == -1 and pos != 0)):
            print("Error: posicao invalida")

        else:
            if self.descritor.init == -1:  # Lista vazia
                self.descritor.init = 0
                self.descritor.fim = 0
            else:
                if self.descritor.fim != self.descritor.maxm - 1:
                    for i in range(self.descritor.fim, self.descritor.init + pos-1, -1):
                        self.elemento[i+1] = self.elemento[i]
                    self.descritor.fim = self.descritor.fim + 1
                else:
                    for i in range(self.descritor.init, self.descritor.init + pos):
                        self.elemento[i-1] = self.elemento[i]
                    self.descritor.init = self.descritor.init-1
            self.elemento[self.descritor.init+pos] = nodo

    def remover(self, pos):
        if pos < 0 or pos > (self.descritor.fim-self.descritor.init):
            return "Error: Impossivel apagar lista vazia"
        else:
            rem = self.elemento[self.descritor.init+pos]
            if pos-self.descritor.init > self.descritor.fim-pos:
                for i in range(self.ini+pos, self.fim):
                    self.elemento[i] = self.elemento[i+1]
                self.elemento[self.descritor.fim] = 0
                self.descritor.fim = self.descritor.fim-1
            else:
                for i in range(self.descritor.init+pos, self.descritor.init, -1):
                    self.elemento[i] = self.elemento[i-1]
                self.elemento[self.descritor.init] = 0
                self.descritor.init = self.descritor.init+1
            return rem

    def destroi(self):
        self.elemento = []
        self.ini = -1
        self.fim = -1


def main():
    l = lista(10)
    print(l.elemento)
    print(l.consultar(2))
    print(l.insere('moto', 0))
    print(l.insere('carro', 1))
    print(l.insere('caminhao', 5))
    print(l.elemento)
    print(l.insere('aviao', 0))
    print(l.elemento)
    print(l.remover(1))
    print(l.elemento)
    print(l.insere("elem", 0))
    print(l.elemento)
    print(l.consultaElement("aviao"))
    l.insereExp("aviaao", "gato")
    print(l.elemento)


def main2():
    l = lista(10)
    l.insere(0, 0)
    l.insere(1, 1)
    l.insere(2, 2)
    print(l.elemento)


main2()
