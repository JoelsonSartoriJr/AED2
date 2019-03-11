class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def subtrair(self):
        return self.a - self.b

    def soma(self):
        return self.a + self.b

    def multiplica(self):
        return self.a*self.b

    def divide(self):
        return self.a/self.b

class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def inicializaData(self):
        if type(self.dia) == int and type(self.mes) == int and type(self.ano) == int:
            if self.dia >= 32 or self.mes > 12 :
                return -1
            else:
                return 1
        else:
            return -1

    def acresentaDias(self, dias):
        if type(dias) == int:
            self.dia = (dias+self.dia)%31
            self.mes += (dias+self.dia)//32
            if self.mes > 12 :
                self.ano += self.mes
                self.mes = self.mes%12
                return self.dia, self.mes, self.ano
            else:
                return self.dia, self.mes, self.ano
        else:
            return -1

    def __str__(self):
        return "Data {}/{}/{}".format(self.dia, self.mes, self.ano)
