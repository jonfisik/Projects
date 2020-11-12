'''
for / else
'''

variavel = ['Luiz Otávio', 'Joazinho', 'Maria']

for item in variavel:
    print(item)

print('-'*15)

for item in variavel:
    if item.startswith('J'):
        print('Começa com J - ', item)
    else:
        print('Não começa com J - ', item)

print('-'*15)
comeca_com_j = False
for item in variavel:
    if item.lower().startswith('j'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J')

print('-'*15)
for item in variavel:
    print(item)
    if item.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J')

