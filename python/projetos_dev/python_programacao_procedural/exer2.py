'''
1 - Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne
o valor da funcao2 executada.
'''


def ola_mundo():
    return 'Hello world!'


def mestre(funcao):
    return funcao()


executando = mestre(ola_mundo)
# Executando uma função dentro de outra
print(executando)
# Mesmo resultado
print(ola_mundo())