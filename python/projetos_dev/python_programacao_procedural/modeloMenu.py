#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__  = 'SBSoltau''JPaschoal'
__version__ = '1.0.0'
__email__   = 'samuel.soltau@unifal-mg.edu.br''jonfisik@hotmail.com'

import readchar

#
# Funções
#
def Traco():
    return print('__'*10)

def Incluir():
    print('Rotina Incluir')
    return

def Consultar():
    print('Rotina consultar')
    return

def Alterar():
    print('Rotina Alterar')
    return

def Excluir():
    print('Rotina Excluir')
    return

def Sair():
    print('Finalizado')
    return

def menu(tipo_menu):
    msgErro = 'Escolha inexistente! Tente novamente.'

    if tipo_menu == 0:
        #menu com opções numéricas
        opcoes = [0,1,2,3,4]
        lista_opcoes = ['(1) Incluir', '(2) Consultar', '(3) Alterar', '(4) Excluir', '(0) Sair']
    elif tipo_menu == 1:
        #menu com opções ASCII
        opcoes = ['I', 'C', 'A', 'E', 'S', 'i', 'c', 'a', 'e', 's']
        lista_opcoes = ['(I) Incluir', '(C) Consultar', '(A) Alterar', '(E) Excluir', '(S) Sair']

    
    while True:
        print('Escolha: ')

        for linha in lista_opcoes:
            print(linha)

        print('Digite a opção desejada: ')

        try:
            #Obtem a opção desejada
            if tipo_menu == 0:
                opcao = int(readchar.readkey())
            elif tipo_menu == 1:
                opcao = readchar.readkey()
                print(opcao)

            if opcao in opcoes:
                break
            else:
                print(msgErro)
        
        except:
            print(msgErro)
            pass
    
    return opcao
#
#Rotina principal
#

def main():
    """
    Menu configuravel:
    0 = Menu com opções numéricas
    1 = Menu com opções caracter ASCII
    """
    Traco()
    print("""[0] Opção numérica.\n[1] Opção caracter.""")
    tipo_menu = int(input("Escolha o tipo de menu: "))
    Traco()

    while True:
        opcao = menu(tipo_menu)

        if tipo_menu == 0:
            if opcao == 0:
                Sair()
                break
            elif opcao == 1:
                Incluir()
            elif opcao == 2:
                Consultar()
            elif opcao == 3:
                Alterar() 
            elif opcao == 4:
                Excluir()
        elif tipo_menu == 1:
            if opcao in ['s', 'S']:
                Sair()
                break
            elif opcao in ['i', 'I']:
                Incluir()
            elif opcao in ['c', 'C']:
                Consultar()
            elif opcao in ['a', 'A']:
                Alterar()
            elif opcao in ['e', 'E']:
                Excluir()

if __name__ == "__main__":
    exit(main())

#EOF