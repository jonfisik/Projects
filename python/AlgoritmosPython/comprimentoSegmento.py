__author__  = 'JPaschoal'
__version__ = '1.0.1'
__email__   = 'jonfisik@hotmail.com'
__date__    = '06/05/2021'
'''
Comprimento segmento
Dados n e uma sequência de n números inteiros, determinar o comprimento de
de um segmento crescente de comprimento.

Exemplos:
Sequência: 5, 10, 3, 2, 4, 7, 9, 8, 5
Comprimento do segmento crescente máximo >>> 4

Sequência 10, 8, 7, 5, 2
Comprimento do segmento crescente máximo >>> 1
'''

#   5, 10, 3, 2, 4, 7, 9, 8, 5
#   ant = 5
#-------------------------------------------
#   prox = 10
#   10 > 5 --> seg + 1
#-------------------------------------------
#   ant = 10
#   prox = 3
#   3 > 10 --> parou
#   --> seg > segMax --> segMax = seg => seg = 1
#--------------------------------------------
#   ant = 3
#   prox = 2
#   2 > 3 --> parou
#   --> seg > segMax --> seg = 1 ...

def traco():
    return print('-----'*10)

print('')
print("SEQUÊNCIA CRESCENTE")
traco()

# input
n = int(input('Digite o tamanho da sequência: '))
ant =int(input('Digite o 1º número da sequência: '))

# váriaveis 
cont = seg = segMax = 1

while cont < n:
    prox = int(input(f'Digite o {cont+1}º número da sequência: '))
    if prox > ant:
        seg += 1
    else:
        if seg > segMax:
            segMax = seg
        seg = 1
        
    
    cont += 1
    ant = prox

print(f'O maior segmento crescente da sequência {segMax}')

traco()
print('')
# END