__author__  = 'JPaschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__date__    = '13/09/2021'
"""
Dados dois naturais m e n determinar, entre todos os pares de números naturais
(x,y) tais que x < m e y < n, um par para o qual o valor da expressão
x*y - x**2 + y seja máximo e calcular também esse máximo.
"""
#-----------------------------------------------------------
def traco():
    return print('-----'*10)

print('')
print("Máximo - ")
traco()

#input
n = int(input('Digite n: '))
m = int(input('Digite m: '))
#-----------------------------------------------------------
Xmax = Ymax = Vmax = 0
x = y = 0

for x in range(m):
    for y in range(n):
        if x*y - x*x + y > Vmax:
            Vmax = x*y - x*x + y
            Xmax = x
            Ymax = y
print('')
print(f'O maior par é {Xmax},{Ymax} e seu valor máximo é {Vmax}.')
traco()
print('')
# END
