from aula17_map import produto, pessoas, lista

# função filter
nova_lista = filter(lambda x: x < 5, lista)
print(lista)
print(nova_lista)
print(list(nova_lista))
print()

# list comprehension
nova_lista = [x for x in lista if x < 5]
print(list(nova_lista))
print()

# Dicionário - filter
print('Preços acima de R$ 30.00')
lista_preco = filter(lambda p: p['preco'] > 30, produto)
for item in lista_preco:
    print(item)
print()

# Com funções
def filtra(produto):
    if produto['preco'] > 30:
        produto['e_caro'] = True
        return True

lista_preco = filter(filtra, produto)

for item in lista_preco:
    print(item)
print()

#
def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

lista_menor = filter(filtra, pessoas)

for item in lista_menor:
    print(item)

