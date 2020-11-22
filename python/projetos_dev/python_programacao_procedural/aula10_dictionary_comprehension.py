'''
dictionary comprehension
'''

def traco(n=30):
    return print('-'*n)

traco()
# Relembrando listas -- multiplicando lista1 por 2
lista1 = [1,2,3,4,5]
lista2 = [v * 2 for v in lista1]
print(lista2)

traco()

lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
]
# Passando lista para dicionário
dic1 = dict(lista)
print(dic1)
# usando dictionary comprehension
#   chave: valor         lista
dic2 = {x: y for x, y in lista}
print(dic2)
dic3 = {x: y*2 for x, y in lista}
print(dic3)

traco()
dic4 = {x.upper(): y.upper() for x, y in lista}
print(dic4)

traco()
dic5 = {x: y for x, y in enumerate(range(5))}
print(dic5)

traco()
# set comprehension
dic6 = {x for x in range(5)}
print(dic6, type(dic6))

traco()
dic7 = {f'chave_{x}': x**2 for x in range(5)}
print(dic7, type(dic7))