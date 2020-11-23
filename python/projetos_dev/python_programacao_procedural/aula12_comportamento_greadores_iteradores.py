'''
comportamento de geradores e iteradores
# lists, tuples and str -> São iteráveis
'''

nome = 'Jona Pant Pas Ama Gomes'

for letra in nome:
    print(letra)
print(nome)

print('-'*15)
iterador = iter(nome)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print('-'*15)

# Itera sobre os elementos que ainda não foram consumidos
for valor in iterador:
    print(valor)
#---------------------------------------
# gerador = (letra for letra in nome)
#
# print(next(gerador))
# print(next(gerador))
# print(next(gerador))
