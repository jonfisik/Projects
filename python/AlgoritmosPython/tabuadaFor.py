__author__  = 'JPaschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__date__    = '01/06/2021'
'''
Tabuada - Paça ao usuário para entrar com início e fim da tabuada.
Imprima a tabuada correspondente dentro dos intervalos considerdos.
Começo  = 1
Fim = 3
Para 1:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3

Para 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6

Para 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
'''
#-----------------------------------------------------------
import time

def traco():
    return print('-----'*10)

print('')
print("TABUADA FOR - ")
traco()

#input
print("Iniciando tabuada...")
time.sleep(1.0)
print('')
comeco = int(input('Começo tabuada:  '))
fim = int(input('Fim tabuada:  '))
#-------------------------------------------------------------

for i in range(comeco, fim+1):
    print('')
    print(f'Para {i}')
    for j in range(comeco, fim+1):
        print(f'{i} x {j} = {i*j}')

print('')
traco()
print('')
# END