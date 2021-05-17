__author__  = 'JPaschoal'
__version__ = '1.0.1'
__email__   = 'jonfisik@hotmail.com'
__date__    = '17/05/2021'
'''
Dados n e n sequências de números inteiros não nulos, cada qual seguida por um 0, calcular a soma dos números
pares de cada sequência.
'''
#-----------------------------------------------------------
import time

def traco():
    return print('-----'*5)

print('')
print("SOMA DOS PARES v1.0.1 - ")
traco()

print("Iniciando ...")
print('')
time.sleep(1.0)

#input
seq = int(input('Digite o número de sequência: '))
print('')
#-------------------------------------------------------------

for i in range(seq):
    print(f'Sequência {i+1}.')
    traco()
    num = int(input("Digite o 1º número da sequência: "))
    soma = cont = 0
    while num != 0:
        if num % 2 == 0:
            soma += num
        cont += 1    
        num = int(input(f'Digite o {cont+1}º número da sequência: '))
    
    print(f'Soma dos pares da sequência {i+1} é {soma}.')
    print('')

        
traco()
print('')
# END