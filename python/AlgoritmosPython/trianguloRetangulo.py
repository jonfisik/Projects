__author__  = 'JPaschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__date__    = '08/06/2021'
"""
Dados três números naturais,
verificar se eles formam os lados de um triângulo retângulo.

lado1**2 + lado2**2 == lado3**2
lado3**2 + lado1**2 == lado2**2
lado2**2 + lado3**2 == lado1**2
"""
#-----------------------------------------------------------
def traco():
    return print('-----'*10)

print('')
print("Triângulo Retângulo - ")
traco()
#input
lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))
#
# Variáveis auxiliares
#
a = lado1**2 + lado2**2 == lado3**2
b = lado3**2 + lado1**2 == lado2**2
c = lado2**2 + lado3**2 == lado1**2
print('')

if a or b or c:
    print('O triângulo é retângulo!')
else:
    print('O triângulo não é retângulo!')

traco()
print('')
# END