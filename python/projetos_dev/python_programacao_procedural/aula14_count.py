'''
count - itertools >>> retorna um iterador
'''

# contador do python - CUIDADO COM O LAÇO INFINITO
from itertools import count

# contador (iterador) infinito
contador = count()

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print()

# Loop infinito com for, count
for valor in contador:
    print(valor)
    if valor >= 10:
        break

print()

#
contador = count(start=5, step=0.1)
for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break
print()

#
contador = count(start=-1, step=-1)
for valor in contador:
    print(round(valor, 2))

    if valor >= 10 or valor <= -10:
        break
print()

# indexar lista
contador = count()
lista = ['Modelo', 'Padrão', 'Partícula', 'Elementares', 'Quark',]

lista = zip(contador, lista)
print(list(lista))