__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '09/01/2022'
'''
"""
Dados x real e n natural, calcular uma aproximação para cos x através dos
n primeiros termos da seguinte série:
cos x = 1/1 - (x**2)/2! + (x**4)/4! - (x**6)/6! + ... + ((-1)**k)*(x**2k)/((2k)!)

#2 termo = 1 termo * -x**2/2*1 --> i = 1 /  2*i = 2 / 2*i - 1 = 1
#3 termo = 2 termo * -x**2/4*3 --> i = 2 / 2*i = 4 / 2*1 - 1 = 3
#4 termo = 3 termo * -x**2/6*5

Compare com os resultados de sua calculadora!
"""
'''
#
## Funções
#
def cosX():
    n = int(input('Digite um valor n para nº de termos: '))
    alfa = float(input('Digite o valor do ângulo alfa: '))

    cos = termo = 1
    for i in range(1, n+1):
        termo *= (-(alfa**2)/(2*i*(2*i-1)))
        cos += termo
    
    return print(f'cos({alfa}) = {cos}')


def traco():
    return print('----'*20)

#
## Título
#
traco()
print('Coseno de X - ')
traco()
#
# Rotina principal
#

resp = 'S'
while resp in 'Ss':
    cosX()
    traco()
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    traco()

print('FIM')
traco()
#END