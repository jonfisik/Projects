__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '04/01/2022'
'''
#ignorância zero
Números reais
Dado um número inteiro positivo n, calcular e imprimir o valor da seguinte soma.

S = 1/n + 2/(n-1) + 3/(n-2)+ ... + n/1
'''

#
## Função e título
# 
def traco():
    return print('----'*7)

traco()
print('Números reais - ')
traco()

#
## input e declaração
# 
n = int(input('Digite um número inteiro: '))

soma = 0.0
for i in range(1, n+1):
    soma += i/(n-i+1)
    print(f'-> {soma}')

traco()
print(f'Soma total: {soma}.')
traco()