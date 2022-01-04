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