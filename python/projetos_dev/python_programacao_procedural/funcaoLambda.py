__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '22/06/2021'
'''
Funções lambda.
lambda nome arg:expressão
'''
def traco():
    print('---'*5)

# Ex1
soma = lambda a,b: a+b
traco()
r = soma(2,6)
print(f'>>> {soma(2,6)}')
print(f'>>> {r}')
traco()

# Ex2
mult = lambda a,b,c:(a+b)*c
m = mult(2,3,6)
print(f'>>> {mult(2,3,6)}')
print(f'>>> {m}')
traco()


# Ex3 - declaração direta
print(f'>>> {(lambda a,b:a+b)(2,3)}')
traco()

# Ex4 - lambda chamando função
r = lambda x,func:x+func(x)
res = r(2, lambda x:x*x)
print(res)
traco()
#FIM