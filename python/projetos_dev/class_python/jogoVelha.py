__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '21/12/2021'
'''
Jogo da velha
Fore, cor da frente / Back, cor da frente / Style, estilo.
'''
import os
import random
from colorama import Fore, Back, Style 

#
#Variáveis globais
#
jogarNovamente = 's'
jogadas = 0
quemJogar = 2
maxJogadas = 9
vit = 'n' #Vitória
velha = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' '],
]

def tela():
    global velha # variável global
    global jogadas
    os.system('cls')
    print('    0   1   2')
    print('0:  ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])
    print('   -----------')
    print('1:  ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])
    print('   -----------')
    print('2:  ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2])
    print('Jogadas: ' + Fore.GREEN + str(jogadas) + Fore.RESET)
    
tela()