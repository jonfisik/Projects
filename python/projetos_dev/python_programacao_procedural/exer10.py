#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Validar cnpj
__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Fisica'
#
#Funções
#
def valida(cnpj):
    digitos = cnpj[12:]
    cnpj = cnpj[:-2] + '0'

    mult = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 0]
    t = 0
    vdigitos = ''

    for a in range(2):
        for i in range(13):
            t += (int(cnpj[int(i)]) * mult[int(i)])
        t = 11 - (t % 11)
        if t > 9:
            t = 0
        vdigitos = vdigitos + (str(t))
        mult.insert(0,6)
        mult.pop()
        cnpj = cnpj[:-1]
        cnpj = cnpj + str(t)
        t = 0
    
    if(vdigitos) == digitos:
        print('Válido')
    else:
        print('Inválido')

#
#Rotina principal
#

try:
    print('\n## Validador de CNPJ ##'
          '\nInforme apenas números\n')
    while True:
        cnpj = input('CNPJ: ')
        if cnpj.isdigit() or len(cnpj) > 14 or len(cnpj):
            print('Inválido')
        else:
            valida(cnpj)
except Exception as erro:
    print(erro)
