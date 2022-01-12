__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '09/01/2022'
'''
"""
#ignorância zero
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

o	Faça um programa que recebe o salário de um colaborador e o
        reajuste segundo o seguinte critério, baseado no salário atual:

o	salários até R$ 280,00 (incluindo) : aumento de 20%
o	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o	salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
o	o salário antes do reajuste;
o	o percentual de aumento aplicado;
o	o valor do aumento;
o	o novo salário, após o aumento.
'''
#
## Funções
# 
def traco():
    print('-----'*15)

def calculoSalario():
    nome = str(input('Funcionário: ')).strip()
    salario = float(input('Salário R$ '))
    traco()
    ajuste = 0
    percentual = str('%')
    if salario <= 280:
        ajuste = salario*0.25
        n_salario = salario + ajuste
        percentual = str('25%')
    elif salario > 280 and salario <= 700:
        ajuste = salario*0.15
        n_salario = salario + ajuste
        percentual = str('15%')
    elif salario > 700 and salario <= 1500:
        ajuste = salario*0.10
        n_salario = salario + ajuste
        percentual = str('10%')
    elif salario > 1500:
        ajuste = salario*0.05
        n_salario = salario + ajuste
        percentual = str('5%')

    print(f'Funcionário: {nome}.')
    print(f'Salário anterior R$ {salario}.')
    print(f'Percentual aplicado {percentual}.')
    print(f'Aumento de R$ {ajuste}.')
    print(f'Novo salário R$ {n_salario}.')

#
## Títulos
#
traco()
print('Cálculo salarial - ')
traco()

#
## Rotina principal
#
opcao = 'S'
while opcao in 'Ss':
    calculoSalario()
    traco()
    opcao = str(input('Deseja continuar cadastro? [S/N] '))
    traco()

print('')
#END