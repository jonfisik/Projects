'''
split, join, enumerete em python
* split - dividir uma string # str -- diferente de sprit - serve para tirar espaços antes e depois
* join - juntar uma lista # str
* enumerete - enumerrar elementos de uma lista # objetos iteráveis
'''
string = 'O Brasil é o país do futebol, o Brasil é penta'
lista1 = string.split(' ') # tira os espaços
lista2 = string.split(',') # vai tirar as vírgulas
print(lista1)
print(lista2)
for item in lista1:
    #print(item)
    print(f'A palavra >> {item} << apareceu {lista1.count(item)}x na frase.')
print('-'*15)
palavra = ''
contagem = 0
for item in lista1:
    qtd_vezes = lista1.count(item)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = item

print(f'A palavra que apareceu mais vezes foi "{palavra}" ({contagem}x).')

print('-'*15)
string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = '-'.join(lista)
print(string)
print(lista)
print(string2)

print('-'*15)
string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, item in enumerate(lista):
    print(indice, '-', item)

print('-'*15)
lista = [[1,2], [3,4], [5,6]]
for i in lista:
    print(i)
    print(i[0])
    print(i[0], i[1])

print('-'*15)
lista = [[0, 'Luiz'], [1, 'João'], [2, 'Maria']]

for indice, nome in lista: # podemos substituir por enumerete (desempacotamento)
    print(indice, nome)

