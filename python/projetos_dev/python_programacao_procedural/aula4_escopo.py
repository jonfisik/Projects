'''
Escopo
'''
def funcao1():
    print(variavel)


def funcao2():
    # global variavel #altera o valor da variavel local
    variavel = 'Local - Outro valor' # variável local
    print(variavel)


def funcao3(arg=None):
    arg = arg.replace('v', 'c')
    return arg

def funcao4():
    outra_variavel = "Luiz Otávio"
    return outra_variavel

def funcao5(arg):
    print(arg)


variavel = 'Global - valor' # variável global

funcao1()
funcao2()
print(variavel)
outra_variavel = funcao3(arg=variavel)
print(outra_variavel)

print('-'*15)

var = funcao4()
funcao5(var)