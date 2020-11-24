'''
Combinatios, Permutations, Product - Itertools
Combinação - ordem não importa
Permutação - Ordem importa
>> Ambos não repetem valores únicos
Produto - Ordem importa e repete valores
'''

from itertools import combinations, permutations, product

pessoas = ['André', 'Tiago', 'João', 'Pedro', 'Mateus']

# Combinação - ordem não importa
cont = 0
for comb in combinations(pessoas, 2):
    print(comb)
    cont += 1
print(f'Total de combinações: {cont}')
print()

# Permutação - ordem importa
cont = 0
for perm in permutations(pessoas, 2):
    print(perm)
    cont += 1
print(f'Total de permutações: {cont}')

# Princípio fundamental da contagem com repetição
cont = 0
for prod in product(pessoas, repeat=2):
    print(prod)
    cont += 1
print(f'Total de permutações: {cont}')