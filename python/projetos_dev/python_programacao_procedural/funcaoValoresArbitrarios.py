__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '22/06/2021'
'''
Funções com argumentos em python.
'''
# Funções

def traco():
    print('--'*20)

def carros(c='Golf'):
    print(f'Modelo - {c}')

# Valores em lista
valores = [1,5,3,2]

def somar(num):
    r = 0
    for i in num:
        r+=i
    
    print(f'Soma da lista  {valores} igual a {r}')
    
# main()

print('')
print('Função - valor default')
traco()
carros('HRV')
traco()
somar(valores)
traco()
print('FIM')

#FIM