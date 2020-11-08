'''
Exercício número par 08-11-2020
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe informe que não é um número inteiro.
'''
def traco():
    print('-'*45)

traco()
print('PAR OU ÍMPAR'.center(45))
traco()

try:
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        print(f'{num} é um número PAR.')
    else:
        print(f'{num} é ímpar!')
except:
    print('ERRO! Não foi digitado um número inteiro.')
traco()