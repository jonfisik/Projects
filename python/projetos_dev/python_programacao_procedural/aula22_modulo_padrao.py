# Módulos padrão do python

## importa o módulo inteiro
import sys
## Verifica em qual plataforma o python está sendo executado
print(f'O python está sendo executado no >>> {sys.platform}.')

# imorta parte do módulo
from sys import platform
print(f'O python está sendo executado no >>> {platform}.')

# imorta parte do módulo por apelido
from sys import platform as SO
print(f'O python está sendo executado no >>> {SO}.')

print()

## Módulo para gerar números aleatórios
#from random import *
## * importa tudo do módulo
import random
for i in range(0,10):
    print(random.randint(0, 10), end=',')

print()

from random import randint
for i in range(10):
    print(randint(0,10), end='-')

print('\n')

## Importando mais de uma função
from random import randint, random
## random() gera números aletórios entre 0 e 1, número de ponto flutuante
for i in range(5):
    print(randint(0, 10), random())

