__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '22/06/2021'
'''
Definição de funções em python.
'''
# Funções

def traco():
    print('--'*20)

def somar(num1, num2):
    res = num1 + num2
    print('Soma de ' + str(num1) + ' e ' + str(num2) + ' = ' + str(res))

# Argumentos arbitrários, com quantos argumentos precisarmos

def texto(*t):
    print(t[0])
    print(t[1])
    print(t[2])

# For irá varrer toda a lista

def textocompleto(*txt):
    for i in txt:
        print(i)

def soma(*adicao):
    r = 0
    for n in adicao:
        r+= n
    
    print(f'Soma = {r}')

def carros(c='Golf'):
    print(f'Modelo - {c}')
    
# main()

print('')
print('Definição Função')
traco()
somar(5,7)
somar(12,8)
somar(1,2)
traco()
texto('Python','Cálculo','Engenharia','Física','Automação')
traco()
textocompleto('Python','Cálculo','Engenharia','Física','Automação')
traco()
soma(2,6,9)
traco()
carros('HRV')
traco()
print('FIM')

#FIM