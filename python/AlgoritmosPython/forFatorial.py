__author__  = 'JPaschoal'
__version__ = '1.0.1'
__email__   = 'jonfisik@hotmail.com'
__date__    = '12/05/2021'
'''
Calcule n! usando o for loop.
5! = 5x4x3x2x1
'''
#-----------------------------------------------------------

def traco():
    return print('-----'*10)

print('')
print("FATORIAL - FOR")
traco()

#input
n = int(input('Digite o valor de n: '))
#
#Calcula o fatorial de n
#Váriaveis 
#
fatorial = 1
#
#for fator in range(2, n+1):
#    fatorial *= fator

for fator in range(n, 1, -1):
    fatorial *= fator

print(f'{n}! é igual a {fatorial}.')

traco()
print('')
# END