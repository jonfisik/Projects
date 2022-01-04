__author__  = 'JPaschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__date__    = '04/01/2022'
"""
#ignorância zero
Dados dois números inteiros positivos i e j diferentes de 0,
imprimir todos os divisores comuns de i e j.

Exemplo: i = 2 e j = 3 a saída deverá ser : 1
i = 9, j = 21 a saída deverá ser: 1, 3
"""

def traco():
    return print('-----'*5)

print('')
print("Divisores de i e j - ")
traco()

#
## input e variáveis
# 
i = int(input('Digite o número i: '))
j = int(input('Digite o número j: '))

nat, cont = 0, 0
#
## teste lógico
#
while cont < i or cont < j:
    if i % cont == 0 and j % cont == 0:
        print('')
        print(f'{i%cont} {j%cont}')
        cont = cont + 1
    nat = nat + 1
print('')
traco()