'''
Funções - def em Python (parte 1)
'''


def funcao():
    print('Hello World!')


def mensagemParamentro(msg):
    print(msg)


def funcaoDoisParametros(msg, nome):
    print(msg, nome)


def funcaoValoresPadrao(msg = 'xxxx', nome = 'xxxxxxx'):
    print(msg, nome)


funcao()
mensagemParamentro('Parâmetro da função')
mensagemParamentro('Outro parâmetro')
funcaoDoisParametros('Olá,', 'Jonatan')
funcaoDoisParametros('Bom dia,', 'Paschoal')
funcaoValoresPadrao()
funcaoValoresPadrao('Boa tarde,', 'Ciclano')
# funções nomeadas, mesmo invertida seguem a ordem quando impressas nas tela
funcaoValoresPadrao(nome = 'Zé', msg = 'Olá,')