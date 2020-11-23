'''
Zip - unindo iteravéis
Zip_longest - Itertools
'''

# Cidades
cidades = ['São Paulo', 'Belém', 'Ananindeua', 'Salvador', 'Bragança', 'Outra']

# Estados
estados = ['SP', 'PA', 'PA', 'BA']

cidade_estados = zip(cidades, estados)
# print(next(cidade_estados))
# print(next(cidade_estados))
# print(next(cidade_estados))
# print(next(cidade_estados))

for valor in cidade_estados:
    print(valor)

print()
cidade_estados = zip(cidades, estados)
print(list(cidade_estados))

print()
cidade_estados = zip(estados, cidades)
print(list(cidade_estados))
#print(dict(cidade_estados))

#-------------------------------------------------
print()
from itertools import zip_longest, count

indice = count()
cidade_estados = zip_longest(estados, cidades,fillvalue='Estado')
print(list(cidade_estados))

print()
cidade_estados = zip(
    indice,
    estados,
    cidades,
)

for indice,estado,cidade in cidade_estados:
    print(indice, estados, cidade)