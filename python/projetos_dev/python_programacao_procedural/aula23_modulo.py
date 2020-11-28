## Módulo
import math
from random import randint
PI = math.pi


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#lista = [1,2,3,4,5]
if __name__ == '__main__':
    print(lista)
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)

