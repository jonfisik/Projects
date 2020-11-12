'''
Listas em Python - fatiamento, append, insert, pop, del, clear, extend, +
min, max
range
nome_da_lista = [] "declaração"
'''
# índice  0    1    2    3    4
lista = ['A', 'Bacana', 'C', 'D', 'E']
#    -    5    4    3    2    1
string = 'ABCD'

print(string[1])
print('-'*10)
print(lista[1])
print('-'*10)
print(lista)
lista[4] = 'Trocou Valor'
print('-'*10)
print(lista)
print('-'*10)
print(lista[0:5:2])
print('-'*10)
print(lista[-1])
print('-'*10)
print(lista[::-1])
print('-'*10)
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(lista1)
print(lista2)
print(lista3)
lista1.extend(lista2) #lista1 estendeu seu tamanho com a lista2
print(lista1,'Com função extend')
lista3.extend('A')
print(lista3,'Com com a função extend')
lista3.append('A')
print(lista3,'Com append')
print('-'*10)
lista1.insert(2, 'maçã')
print(lista1)
lista1.pop() # remove o último elemento
print(lista1)
print('-'*10)
lista4 = [1,2,3,4,5,6,7,8,9]
print(lista4)
del(lista4[3:5])
print(lista4)
print('-'*10)
print(lista2)
print(max(lista2))
print(lista4)
print(min(lista4))
print('-'*10)
lista5 = list(range(1,101,1)) # lsista é iterável
print(lista5)
for item in lista5:
    print(item)
print('-'*10)
soma = 0
for item in lista5:
    soma = soma + item
print(soma)
print('-'*10)
lista6 = ['string', True, 1, 20.5]
for elem in lista6:
    print(f'O tipo do elemento >> {elem} << é {type(elem)}.')