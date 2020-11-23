'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma llista for maior que a outra, a soma só vai cosniderar o tamanho da menor

ex.:
lista_A = [1,2,3,4,5,6,7]
lista_B = [1,2,3,4]
====== Resultado
lista_soma = [2,4,6,8]
'''

# Solução genérica
lista_A = [1, 2, 3, 4, 5, 6, 7]
lista_B = [1, 2, 3, 4]

lista_soma = []
for i in range(len(lista_B)):
    lista_soma.append(lista_A[i] + lista_B[i])
# print(f'Lista A {lista_A} + Lista B {lista_B} = {lista_soma}')
print(lista_soma)

print()

# usando funções do python
lista_soma =[]
for i, _ in enumerate(lista_B):
    lista_soma.append(lista_A[i] + lista_B[i])
print(lista_soma)

print()
# Forma exclusiva python,com união de listas

lista_soma = [x + y for x, y in zip(lista_A, lista_B)]

print(lista_soma)

print()
# unindo as listas A e B
print(list(zip(lista_A, lista_B)))

print()
# usando o método zip_longest - para pegar os valores da lista maior

from itertools import zip_longest

lista_soma = [x + y for x, y in zip_longest(lista_A, lista_B, fillvalue=0)]

print(lista_soma)