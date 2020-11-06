'''
Condicionais IF, ELIF e ELSE -
'''
print('-'*30)
x = int(input('Digite um número x: '))
y = int(input('Digite um número y: '))
print('-'*30)
if x > y:
    print(f'{x} é MAIOR que {y}.'.center(30))
elif x == y:
    print(f'{x} é IGUAL a {y}.'.center(30))
else:
    print(f'{x} é MENOR que {y}.'.center(30))
print('-'*30)
