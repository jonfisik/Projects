__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '13/01/2022'
import random
#random.randrange(start, stop[, step])
"""
Retorna aleatóriamente um elemento de range(começo, fim, passo).
Isso é equivalente a choice(range(começo, fim, passo)), mas não constrói um
objeto range.
"""
#print(f'{variavel}', '->', end = '')
def traco():
    print('-----'*3)

#Exemplo
#print('random.randrange(start, stop[, step])')
#for i in range(10):
    #x = random.randrange(1,7)
    #x = random.randrange(1, 7, 2)
    #print(x)

##################################################################

#random.randint(a, b)
"""
Retorna um inteiro N de tal forma que a <= N <= b.
Tal como randrange(a, b+1).
"""
#Exemplo
"""
print('random.randint(a, b)')
for i in range(10):
    x = random.randint(1,7)
    print(x)
"""

##################################################################

#random.choice(seq)
"""
Retorna um elemento aleatória de uma sequência não-vazia.
Se recebe uma sequência vazia devolve um erro do tipo IndexError.
"""
#Exemplo
"""
print('random.choice(seq)')
for i in range(10):
    x = random.choice([1.7, 2.3, 3, 4, 5, 6])
    #x = random.choice(range(1, 7))
    print(x)
"""

##################################################################

#random.random()
"""
Retorna um real entre 0.0 e 1.0.
"""
#Exemplo
"""
print('random.random()')
for i in range(10):
    print(random.random())
"""

##################################################################

#random.uniform(a, b)
"""
Retorna um real N tal que a <= N <= b ou b <= N <= a.
"""
#Exemplo
"""
print('random.uniform(a, b)')
for i in range(10):
    #x = random.uniform(1, 7)
    #x = random.uniform(7, 1)
    print(x)
"""
