__author__  = 'JPaschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__date__    = '04/01/2022'
"""
#ignorância zero
Dado n e dois números inteiros positivos i e j diferentes de 0, imprimir em ordem crescente os n primeiros naturais que são múltilpos de i ou de j e ou ambos.

Exemplo: Para n = 6, i = 2 e j = 3 a saída deverá ser: 0, 2, 3, 4, 6, 8.
"""

def traco():
    return print('-----'*5)

print('')
print("Multiplos até N - ")
traco()

#
## input e variáveis
# 
n = int(input('Digite N: '))
i = int(input('Digite o número i: '))
j = int(input('Digite o número j: '))

nat, cont = 0, 0
#
## teste lógico
#
while cont < n:
    if nat % i == 0 or nat % j == 0:
        print('')
        print(f'-> {nat}')
        cont = cont + 1
    nat = nat + 1
print('')
traco()