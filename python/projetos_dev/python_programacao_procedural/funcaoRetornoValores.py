__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '22/06/2021'
'''
Funções com retorno de valores.
'''
def traco():
    print('---'*10)

valores=[1,5,3,2,10,50,-100]

def somar(num):
    r = 0
    for n in num:
        r += n
    # a função retornará o valor de r, r  é uma variável local
    return r

def valLista(num):
    for v in num:
        print(v)


traco()
valLista(valores)
print(f'Dado os valores {valores} - Soma = {somar(valores)}.')
traco()
#FIM