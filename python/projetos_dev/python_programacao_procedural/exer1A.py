'''
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
'''
def saudacao(saud, nome):
    print(f'{saud}, {nome}.')

def traco(x=10):
    print('--'*x)

traco(15)
x = str(input('Digite uma saudação: '))
y = str(input('Digite um nome: '))
saudacao(x, y)
traco(15)