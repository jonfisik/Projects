__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '22/06/2021'
'''
Definição de funções em python.
'''

n1 = 15
n2 = 7

def traco():
    print('--'*20)

def somar():
    res = n1 + n2
    print('Soma de ' + str(n1) + ' e ' + str(n2) + ' = ' + str(res))

def subtrair():
    res = n1 - n2
    print('A diferença de ' + str(n1) + ' e ' + str(n2) + ' = ' + str(res))

def multiplicar():
    res = n1 * n2
    print('O produto de ' + str(n1) + ' e ' + str(n2) + ' = ' + str(res))


def calculos():
    somar()
    subtrair()
    multiplicar()

# main()

print('')
print('Definição Função')
traco()
somar()
subtrair()
multiplicar()
traco()
print('')
calculos()
traco()

#END