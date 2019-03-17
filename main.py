#from TADNumero import Data

#t = Data(31,2,1990)
#print(t.inicializaData())
#print(t.escreveExtenso())
#print(t.acresentaDias(100))

from TADNumero import Fila

f = Fila()
f.inserir('joao', 127689)
f.escreve()
f.inserir('Maria', 117689)
f.escreve()
f.excluir()
f.escreve()