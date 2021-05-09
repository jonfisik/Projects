__author__  = 'JPaschoal'
__version__ = '1.0.1'
__email__   = 'jonfisik@hotmail.com'
__date__    = '08/05/2021'
'''
Dados n e uma sequência de números inteiros, determinar quantos segmentos de
números iguais consecutivos compõem essa sequência.

Exemplos:
Sequência: 5, 2, 2, 2, 4, 4, 4, 4, 1, 1
Comprimento do segmento igual >>> 5
'''
#   5, 2, 2, 2, 4, 4, 4, 4, 1, 1
#   ant = 5
#   seg = 1
#   n = 10
#   cont = 0
#-------------------------------------------
#   prox = 2
#   ant == prox --> 
#   ant != prox --> seg += 1
#   ant = prox = 2
#-------------------------------------------
#   ant = 2
#   prox = 2
#   ant == prox 
#   ant = prox
#--------------------------------------------

def traco():
    return print('-----'*10)

print('')
print("SEQUÊNCIA IGUAL")
traco()

# input
n = int(input('Digite o tamanho da sequência: '))
ant =int(input('Digite o 1º número da sequência: '))

# váriaveis 
cont = seg = 1

while cont < n:
    prox = int(input(f'Digite o {cont+1}º número da sequência: '))
    if prox != ant:
        seg += 1
    ant = prox
    cont += 1

print(f'A sequência tem {seg} segmento(s) iguais.')

traco()
print('')
# END