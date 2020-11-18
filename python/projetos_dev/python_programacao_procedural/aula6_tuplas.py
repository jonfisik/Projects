'''
Tuplas
'''
tupla1 = (1,2,3,4,5,6, 'Jon') * 2
print(tupla1)
print(type(tupla1))
print(tupla1[6])

for indice, item in enumerate(tupla1):
    print(indice, '-', item) # iteração de tuplas

print(tupla1[3:])

print('-'*15)

tupla2 = 1,2,3,'a','b' # Tupla criada sem parênteses
print(tupla2)

print('-'*15)

tupla3 = 1, # Tupla com um elemento
print(tupla3, type(tupla3))

tupla3 = (1,2,3,50)
tupla4 = (4,'Jon',6,100)

tupla5 = tupla3 + tupla4
print(tupla5)
n1, n2, n3, *_, n15 = tupla5
print(tupla5)
print(n15)
print(tupla5*3)
print('-'*15)
lista = tupla1 = list(tupla1)
print(lista)
lista[3] = 'Amanda'
print(lista)

