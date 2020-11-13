'''
Validador de CPF
CPF = 168.995.350-09
--------------------------------------------
1 * 10 = 10          #    1 * 11 = 11  <-
6 * 9  = 54          #    6 * 10 = 60
8 * 8  = 64          #    8 *  9 = 72
9 * 7  = 63          #    9 *  8 = 72
9 * 6  = 54          #    9 *  7 = 63
5 * 5  = 25          #    5 *  6 = 30
3 * 4  = 12          #    3 *  5 = 15
5 * 3  = 15          #    5 *  4 = 20
0 * 2  = 0           #    0 *  3 = 0
                     #->  0 *  2 = 0
        297          #             343
11 - (297 % 11) = 11 #     11 - (343 % 11) = 9
11 > 9 = 0           #
Digito 1 = 0         #  Digito 2 = 9
'''
print('-'*20)
lista1_cpf = [1,6,8,9,9,5,3,5,0]

soma = 0
for i, j in enumerate(lista1_cpf):
    print(f'{i+1}) {j} x {10-i} = {j * (10-i)}')
    soma = soma + (j * (10-i))
print('-'*20)
print(f'Soma = {soma}')

teste = 11 - (soma % 11)
if teste > 9:
    print('Digito 1 >> 0.')
else:
    print('CPF inválido.')

print('-'*20)
lista2_cpf = [1,6,8,9,9,5,3,5,0,0]

soma = 0
for i, j in enumerate(lista1_cpf):
    print(f'{i+1}) {j} x {11-i} = {j * (11-i)}')
    soma = soma + (j * (11-i))
print('-'*20)
print(f'Soma = {soma}')

teste = 11 - (soma % 11)
if teste == 9:
    print('Digito 2 >> 9.')
else:
    print('CPF inválido.')
print('-'*20)