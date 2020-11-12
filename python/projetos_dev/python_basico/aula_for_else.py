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
    if item.startswith('J'):
        comeca_com_j = True

if comeca_com_j:
    print()
