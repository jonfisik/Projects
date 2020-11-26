'''
reduce -
'''

from aula17_map import produto, pessoas, lista
from functools import reduce

# usando acumulador
acumula = 0
for item in lista:
    acumula += item

print(f'Valores acumulados - {acumula}')
print()

# usando função reduce
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(f'Valores acumulados - {soma_lista}')
print()

# Dicionário
soma_preco = reduce(lambda ac, p: p['preco'] + ac, produto, 0)
print(f'Valores somados - R$ {soma_preco}.')
print(f'Média de preços - R$ {soma_preco/len(produto)}.')
print()

#
soma_idades = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(f'Média da idade das pessoas: {round(soma_idades/len(pessoas), 2)}')
