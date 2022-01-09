__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '09/01/2022'
'''
"""
"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia um conjunto indeterminado de temperaturas, e informe
ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.

7, 5, 3524, 5, 5, 7, 67, 2, 78
"""
'''
#
## Funções
#
def temperaturaCompara():
    n = int(input('Digite o número de temperatura: '))
    soma = maior = menor = float(input('Digite a 1º temperatura: '))

    #temp = 0
    for i in range(2, n+1):
        temp = float(input(f'Digite a {i}º temperatura: '))
        
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp

        soma += temp
    traco()
    print(f'A maior temperatura é {maior:4.1f}C.') # :4.1f. Alinha com quatro casas / ou g: notação científica. 
    print(f'A menor temperatura é {menor:4.1f}C.')
    print(f'A média das temperaturas é {soma/n:4.1f}C.')


def traco():
    return print('----'*10)

#
## Título
#
traco()
print('Temperatura Maior, menor - ')
traco()

#
# Rotina principal
#
resp = 'S'
while resp in 'Ss':
    temperaturaCompara()
    traco()
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    traco()

print('FIM')
traco()
#END