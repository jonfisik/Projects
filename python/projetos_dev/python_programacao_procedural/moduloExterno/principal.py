__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '22/12/2021'
'''
Arquivo principal
'''
#import funcaoModuloExterno
#from funcaoModuloExterno import jogador
import funcaoModuloExterno as fm

#funcaoModuloExterno.canal()
#print(funcaoModuloExterno.jogador['nome'])
#print(jogador['nome'])

fm.canal()
print(fm.jogador['nome'])

print(' ')

# dir: mostra o que tem dentro do módulo que está separado
mostra = dir(fm) 
print(mostra)

print(' ')