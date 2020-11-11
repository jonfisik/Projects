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