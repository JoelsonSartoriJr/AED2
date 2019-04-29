from linkList import LinkedList

#Exerc 1
lista = LinkedList()
lista.append(7)
lista.append(8)
lista.append(9)
lista.append(10)
lista.append(11)
print(len(lista))

#Exerc 2
lista2 = LinkedList()
lista2.append(7)
lista2.append(8)
lista2.append(9)
lista2.append(10)
lista2.append(11)
print(lista.compara(lista2))

#Exerc3
print(lista)
print(lista.reverse())

#Exerc4
print(lista.maiorMedia())