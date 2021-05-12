__author__  = 'JPaschoal'
__version__ = '1.0.2'
__email__   = 'jonfisik@hotmail.com'
__date__    = '12/05/2021'
'''
Um número triangular é calculado pela fórmula triangular = n*(n+1)//2.
Sendo n o índice desse número triangular
Escreva um programa que imprima os números tringulares com índices múltiplos de 5 entre 5 e 50.
'''
#-----------------------------------------------------------

def traco():
    return print('-----'*10)

print('')
print("TRIANGULAR - FOR")
traco()

#input
m = int(input('Digite o valor de inicial: '))
n = int(input('Digite o valor de para calcular: '))
mult = int(input('Múltiplo de quanto? '))
#
#Calcula número triangular
#Váriaveis 
#
for n in range(m, n+1, mult):
    triangular = n*(n+1)//2 # divisão inteira
    print(f'Para n = {n} número triangular = {triangular}.')

traco()
print('')
# END