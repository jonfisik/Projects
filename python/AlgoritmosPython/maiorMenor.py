__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '12/01/2022'
'''
"""
#ignorância zero
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''
#
## Funções
# 
def traco():
    print('-----'*15)

def comparando():
    num_maior = num_menor = int(input('1º Número: '))
    alt_maior = alt_menor = float(input('Altura (cm): '))
    traco()
    for i in range(9):
        num = int(input(f'{i+2}º Número: '))
        alt = float(input('Altura: '))
        traco()
        if alt < alt_menor:
            alt_menor = alt
            num_menor = num
        if alt > alt_maior:
            alt_maior = alt
            num_maior = num
    print(f'O aluno de número {num_maior} tem a maior altura >>> {(alt_maior/100):.2f} m.')
    print(f'O aluno de número {num_menor} tem a maior altura >>> {(alt_menor/100):.2f} m.')
#
## Títulos
#
traco()
print('Comparando altura - ')
traco()

#
## Rotina principal
#
opcao = 'S'
while opcao in 'Ss':
    comparando()
    traco()
    opcao = str(input('Deseja continuar cadastro? [S/N] '))
    traco()

print('')
#END