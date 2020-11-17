'''
Funções Lambda (anônimas)
'''
def linha(n=10):
    print('*-*' * n)


def produto(num1, num2):
    return num1 * num2


linha(12)
a = 2
b = 5
resp = produto(a, b)
print(f'Resultado da função produto {a} x {b} = {resp}')
linha(12)
resp2 = lambda a, b: a * b
print(f'Resultado da função Lambda {a} x {b} = {resp}')
linha(12)
lista = [
    ['prod1', 36],
    ['prod2', 6],
    ['prod3', 50],
    ['prod4', 25],
    ['prod5', 69],
    ['prod6', 100]
]


def funcao(item):
    '''
    Ordenando pelo índice da lista
    :param item:
    :return:item[?]
    '''
    return item[1]


print(lista)
lista.sort(key=funcao)
#lista.sort(key=funcao, reverse=True)
print(lista)
lista.sort(key=lambda item: item[1])
print(lista)
print(sorted(lista, key=lambda i: i[1], reverse=True))