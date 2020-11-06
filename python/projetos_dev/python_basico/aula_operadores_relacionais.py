'''
Operadores realcionais
== > >= =< < !=
'''
print('-'*30)
print('COMPARANDO NÚMEROS'.center(30))
print('-'*30)
opcao = int(input('''[1] Para números reais
[2] Para números inteiros
Opção: '''))
print('-'*30)
if opcao == 1:
    x = int(input('Digite um número inteiro x: '))
    y = int(input('Digite um número inteiro y: '))
elif opcao == 2:
    x = float(input('Digite um número real x: '))
    y = float(input('Digite um número real y: '))

print('-'*30)
if x > y:
    print(f'{x} é MAIOR que {y}.'.center(30))
elif x == y:
    print(f'{x} é IGUAL a {y}.'.center(30))
else:
    print(f'{x} é MENOR que {y}.'.center(30))
print('-'*30)

v = True
if (x > y) == v:
     a = 'Verdadeiro'
else:
     a = 'Falso'

#a = (x > y) == v if 'Verdadeiro' else 'Falso' # está voltando True, False
#a = 'Verdadeiro' if (x > y) == v else 'Falso'

if (x == y) == v:
    b = 'Verdadeiro'
else:
    b = 'Falso'

#b = 'Verdadeiro' if (x == y) == v else 'Falso'

if (x < y) == v:
    c = 'Verdadeiro'
else:
    c = 'Falso'

#c = 'Verdadeiro' if (x < y) == v else 'Falso'

print(f'-- {x} > {y}: {a}.')
print(f'-- {x} = {y}: {b}.')
print(f'-- {x} < {y}: {c}.')

print('-'*30)