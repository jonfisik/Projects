__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '09/01/2022'
'''
"""
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
'''
#
## Funções
#
def mediaTurmas():
    turmas = int(input('Digite a quantidade de turmas: '))
    soma = 0
    for i in range(1, turmas+1):
        qtd = int(input(f'Digite o número de alunos da {i}ª turma: '))

        while qtd > 40 or qtd < 0:
            print('Número de alunos inválido.')
            qtd = int(input(f'Digite o número de alunos da turma {i}ª turma: '))
        soma += qtd
    print (f'A média dos alunos é {soma/turmas:.10g}')

def traco():
    return print('----'*10)

#
## Título
#
traco()
print('Media de alunos - ')
traco()

#
## Rotina principal
#

opcao = 'S'
while opcao in 'Ss':
    mediaTurmas()
    traco()
    opcao =str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    traco()

print('FIM')
traco()
#END