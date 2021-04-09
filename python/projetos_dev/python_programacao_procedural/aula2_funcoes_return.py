'''
Funções (def) em Python - return - Parte 2
'''

def funcao(var):
    #print(var)
    return var
    # A partir daqui nada será executado dentro dessa função.


def divisao(n1, n2):
    #if n2 > 0:
        #return n1 / n2
    if n2 == 0:
        return
    return n1 / n2

# Função atribuida a uma variável, não retornará none
variavel = funcao('Valor que eu quero.')

if variavel:
    print(variavel)
else:
    print('Nenhum Valor.')

divide = divisao(8,10)

if divide:
    print(divide)
else:
    print('Conta inválida.')

print('-'*20)
def f(var):
    print(var)


def dumb():
    return f


var = dumb()
print(id(var), id(f))

if var == f:
    print('var é igual a f.')
else:
    print('Blaaaaaaa')

