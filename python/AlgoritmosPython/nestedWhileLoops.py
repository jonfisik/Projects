__author__  = 'JPaschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
#
# Definição  "Nested while loops"
#
'''
i = 0
n = 5
while i < n:
    j = 0
    while j < n:
        print(i, j) 
        j = j + 1
    i = i + 1
'''
'''
Dado um número n de empresas, e um número m de meses, e o ganho e gastos positivos e inteiros de cada empresa para cada mês, imprimir se a empresa  nesses meses ficou com déficit, lucro ou indiferente e imprimir o valor  correspondente a essa balança.
'''
print('')
n = int(input('Digite o número de empresas: '))
m = int(input('Digite o número de meses: '))

empresa = 1
print('')
while empresa <= n:
    mes = 1
    balanca = 0
    print('Empresa', empresa,":")
    while mes <= m:
        print('Mês', mes,":")
        ganho = int(input('Digite o ganho da empresa no mês: '))
        gasto = int(input('Digite o gasto da empresa no mês: '))
        balanca = balanca + (ganho - gasto)
        print("")
        mes = mes + 1

    if balanca == 0:
        print('A empresa ', empresa,'ficou indiferente (balança = 0)')
    elif balanca > 0:
        print('A empresa ', empresa,'fechou com lucro de R$', balanca)
    else:
        print('A empresa ', empresa,'fechou com déficit de R$', balanca)
    empresa = empresa + 1
    print("")

print('-FIM ANÁLISE-')
print("")