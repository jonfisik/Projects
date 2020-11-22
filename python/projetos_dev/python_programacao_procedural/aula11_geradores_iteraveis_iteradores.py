'''
geradores, iteraveis, iteradores
'''
# objeto iterável
lista = [1, 2, 3, 4, 5]
print(lista, ' - Lista - Obj iterável: ', hasattr(lista, '__iter__'))
string = 'Texto'
print(string, ' - String - Obj iterável: ', hasattr(string, '__iter__'))
numero = 123456
print(numero, ' - Número - Obj iterável: ', hasattr(numero, '__iter__'))
print()
# FOR transforma a lista em iterador
for i in lista:
    print('Lista em iterador')
    print(i)
print()
# método para iterador
print(lista, ' - Lista - iterador: ', hasattr(lista, '__next__'))

# Objeto iterável não é necessariamente um iterador
lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print()

# Geradores
import sys
import time
lista = list(range(10))
# sys.getsizeof() - mostra quanto bytes de memória está sendo consumido
print(f'Memória consumida na lista {lista} - \n', sys.getsizeof(lista), 'bytes')

print()
# simulando processamento pesado
def gera():
    r = []
    for n in range(10):
        r.append(n)
        time.sleep(0.01)
    return r

g = gera()

for v in g:
    print(v)

print()

def geracao_por_vez():
    for n in range(10):
        yield n
        time.sleep(0.3)

g = geracao_por_vez()

for v in g:
    print(v)

print()
# iteradores são iteráveis
print(hasattr(g, '__iter__')) # iterável
print(hasattr(g, '__next__')) # iterador

print()

g = geracao_por_vez()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print()

# gerador -  a cada chamada mostra o valor na sequência
def gerador():
    variavel = 'valor 1'
    yield variavel
    time.sleep(0.5)
    variavel = 'valor 2'
    yield variavel
    time.sleep(0.5)
    variavel = 'valor 3'
    yield variavel
    time.sleep(0.5)

h = gerador()

# print(next(h))
# print(next(h))
# print(next(h))

for v in h:
    print(v)

print()

# lista
l1 = [x for x in range(950)]
print(l1, type(l1))

print()

# gerador
l2 = (x for x in range(950))
print(next(l2), type(l2))
print(next(l2), type(l2))
print(next(l2), type(l2))

print()

for v in l2:
    print(v)

print()
# tamanho
print('Lista', sys.getsizeof(l1))
print('Gerador', sys.getsizeof(l2))