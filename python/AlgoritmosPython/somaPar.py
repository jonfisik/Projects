__author__  = 'JPaschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__date__    = '01/06/2021'
'''
Soma par - Dados n de n sequências de números inteiros não nulos, cada qual seguida por um 0, calcular a soma dos números pares de cada sequência.
'''
#-----------------------------------------------------------
def traco():
    return print('-----'*10)

print('')
print("SEQUÊNCIAS - ")
traco()

#input
n = int(input('Digite o número de sequências >> '))
#-----------------------------------------------------------

for i in range(n):
    print('')
    print(f'Sequência {i+1}.')
    num = int(input('Digite o 1º número da sequência: '))
    soma = 0
    cont = 1
    while num != 0:
        if num % 2 == 0:
            soma += num
        num = int(input(f"Digite o {cont+1}º número da sequência >> "))
        cont += 1    
    print(f'A soma da sequência {i+1} é {soma}.')


print('')
traco()
print('')
# END