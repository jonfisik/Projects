'''
Funções (def) em Python - *args **kwarg -
'''
def func(a1,a2,a3,a4,a5,nome='None',a6=None): # depois de um argumento nomeado, todos os outros serão nomeados tbm
    print(a1,a2,a3,a4,a5,nome,a6)
    return nome, a6

var = func(1,2,3,4,5,nome = 'Jon', a6 = '6')

def desempacotamento(*args, **kwargs): # * usado para vários argumentos (desempacotamento) / kwargs = usado com chave
    print(args)
    #print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])


lista = [1, 2, 3, 4, 5]
lista2 = [9, 8, 7, 6]
n1, n2, *n = lista
print(n1, n2, n)
desempacotamento(lista)
print(*lista)
print(*lista, sep='-')
desempacotamento(n1)
desempacotamento(*lista, 6, 7, 8, 9, 10, 11, 12)
desempacotamento(lista, *lista2)
desempacotamento(*lista, *lista2)
desempacotamento(*lista2, nome='jona', sobrenome='pantoja')