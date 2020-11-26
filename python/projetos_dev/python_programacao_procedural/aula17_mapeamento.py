from aula17_map import produto, pessoas, lista

# Lista - map
print(lista)
print()

# (função) map - retorna um iterador
nova_lista = map(lambda x: x * 3, lista)
print(nova_lista)
print(list(nova_lista))
print()

# list comprehension
nova_lista_comprehension = [x * 3 for x in lista]
print(nova_lista_comprehension)
print()

# Dionário - map
for item in produto:
    print(item)
print()

# Mostrar os preços do dicionário
precos = map(lambda p: p['preco'], produto)

for item in precos:
    print(item)
print()

# Preço modificado
def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 3)
    return p

novo_produto = map(aumenta_preco, produto)

for item in novo_produto:
    print(item)
print()

#
for item in pessoas:
    print(item)
print()
#
nomes = map(lambda p: p['nome'], pessoas)
for item in nomes:
    print(item)
print()
#
idades = map(lambda i: i['idade'], pessoas)
for item in idades:
    print(item)
print()
#
def aumenta_idade(i):
    i['nova_idade'] = i['idade'] + 5
    return i

idade = map(aumenta_idade, pessoas)

for item in idade:
    print(item)
print()

