__author__  = 'JPaschoal'
__version__ = '1.0.1'
__email__   = 'jonfisik@hotmail.com'
__date__    = '17/05/2021'
'''
Peça para o usuário entrar com início e o fim da tabuada
e imprima a tabuada correspondente dentro dos intervalos
considerados.
Começo = 1
Fim = 3

Tabuada do 1
1x1 = 1
1x2 = 2
1x3 = 3

Tabuada do 1
2x1 = 2
2x2 = 4
2x3 = 6

Tabuada do 1
3x1 = 3
3x2 = 6
3x3 = 9
'''
#-----------------------------------------------------------
import time

def traco():
    return print('-----'*5)

print('')
print("TABUADA BLOCO v1.0.1 - ")
traco()


print("Iniciando tabuada...")
print('')
time.sleep(1.0)

#input
comeco = int(input('Digite o começo da tabuada: '))
fim = int(input('Digite o fim da tabuada: '))
#-------------------------------------------------------------

for i in range(comeco, fim+1):
    traco()
    print(f'Tabuada do {i}.')
    for j in range(comeco, fim+1):
        print(f'{i} X {j} = {i*j}')
        
traco()
print('')
# END