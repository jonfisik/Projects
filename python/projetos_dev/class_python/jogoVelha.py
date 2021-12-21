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
quemJoga = 2 # 1 = CPU - 2 = Jogador
maxJogadas = 9
vit = 'n' #Vitória
velha = [
    [' ',' ',' '], # L0C0 L0C1 L0C2
    [' ',' ',' '], # L1C0 L1C1 L1C2
    [' ',' ',' ']  # L2C0 L2C1 L2C2
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

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input('Linha..: ')) 
            c = int(input('Coluna.: '))
            while velha[l][c] != ' ':
                l = int(input('Linha..: ')) 
                c = int(input('Coluna.: '))
            velha[l][c] = 'X'
            quemJoga = 1
            jogadas += 1
        except:
            print('')
            print('JOGADA INVÁLIDA!')
            os.system('pause')
 
def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha[l][c] != ' ':
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        velha[l][c] = 'O'
        jogadas += 1
        quemJoga = 2

def verificarVitoria():
    global velha
    vitoria = 'n'
    simbolos = ['X','O']
    for s in simbolos:
        vitoria = 'n'
        #Verificar Linhas
        indice_linha = indice_coluna = 0
        while indice_linha < 3:
            soma = 0
            indice_coluna = 0
            while indice_coluna < 3:
                if (velha[indice_linha][indice_coluna] == s):
                    soma += 1
                indice_coluna += 1
            if(soma == 3):
                vitoria = s
                break
            indice_linha += 1
        if(vitoria != 'n'):
            break

        #Verificar Colunas
        indice_linha = indice_coluna = 0
        while indice_coluna < 3:
            soma = 0
            indice_linha = 0
            while indice_linha < 3:
                if (velha[indice_linha][indice_coluna] == s):
                    soma += 1
                indice_linha += 1
            if(soma == 3):
                vitoria = s
                break
            indice_coluna += 1
        if(vitoria != 'n'):
            break

        #Verificar Diagonal 1
        soma = 0
        idiag = 0 # idiag: indice diagonal
        while idiag < 3:
            if(velha[idiag][idiag] == s):
                soma += 1
            idiag += 1
        if(soma == 3):
            vitoria = s
            break

        #Verificar Diagonal 2
        soma = 0
        idiagl = 0 # idiagl: indice diagonal linha
        idiagc = 2 # idiagc: indice diagonal coluna
        while idiagc < 3:
            if(velha[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if(soma == 3):
            vitoria = s
            break
    return vitoria

while True:
    tela()
    jogadorJoga()
    cpuJoga()