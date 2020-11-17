'''
2 - Crie uma funcao1 que receba uma funcao2 como parâmetro e retorne o valor da funcao2
executada. Faça a funcao1 executar duas funções que recebam um número diferente de argumentos.
--- Melhor do que executar duas ou mais funções executa-se apenas uma.
'''

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Jon')
print(executando)
print('-'*15)
executando = mestre(saudacao, 'Jon', saudacao='Hello,')
print(executando)