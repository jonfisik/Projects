__author__  = 'JPaschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__date__    = '08/06/2021'
"""
"""
Dados três números naturais,
verificar se eles formam os lados de um triângulo retângulo.

lado1**2 + lado2**2 == lado3**2
lado3**2 + lado1**2 == lado2**2
lado2**2 + lado3**2 == lado1**2
"""
"""
#-----------------------------------------------------------
def traco():
    return print('-----'*10)

print('')
print("Par máximo - ")
traco()
#input
n = int(input('Digite n: '))
m = int(input('Digite m: '))

Xmax = Ymax = Vmax = 0

x = y = 0
for x in range(m):
    for y in range(n):
       #?print(f'{x},{y}')
        if x*y - x*x + y > Vmax:
            Vmax =  x*y - x*x + y
            Xmax = x
            Ymax = y
    #?print(f'{x},{y}')
print(f'O maior par é ({Xmax}, {Ymax}) e seu valor máximo é {Vmax}.')

#-----------------------------------------------------------



print('')
traco()
print('')
# END