__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '04/01/2022'
'''
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer
as consistências, informando ao usuário nas seguintes situações:

    a.	Se o usuário informar o valor de A igual a zero, a equação não é do
    segundo grau e o programa não deve fazer pedir os demais valores,
    sendo encerrado;

    b.	Se o delta calculado for negativo, a equação não possui raizes reais.
    Informe ao usuário e encerre o programa;

    c.	Se o delta calculado for igual a zero a equação possui apenas uma raiz
    real; informe-a ao usuário;

    d.	Se o delta for positivo, a equação possui duas raiz reais; informe-as
    ao usuário;

delta = b**2 - 4*a*c
raiz = (-b +ou-(delta**(1/2)))/(2*a)
'''
#
## Funções
#
def traco():
    return print('----'*20)

#
## Título
#
traco()
print('Equação do 2º grau - ')
traco()

a = float(input('Digite o coeficiente [a]: '))
b = float(input('Digite o coeficiente [b]: '))
c = float(input('Digite o coeficiente [c]: '))
print(f'Equação a ser resolvida {a}x2+{b}x+{c}=0')

delta = b**2 - 4*a*c
if a == 0:
    print('A equação informada não é do segundo grau.')
else:
    if delta < 0:
        print('Delta negativo, não há raízes nos reais.')
    elif delta == 0:
        raiz1 = (-b+(delta**(1/2)))/(2*a)
        print(f'Delta igual a zero, há apenas uma raíz x1 = {raiz1}.')
    elif delta > 0:
        raiz1 = (-b+(delta**(1/2)))/(2*a)
        raiz2 = (-b-(delta**(1/2)))/(2*a)
        print(f'Delta positivo, há duas raízes x1 = {raiz1} e x2 = {raiz2}.')
traco()