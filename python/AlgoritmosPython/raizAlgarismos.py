__author__  = 'JPaschoal'
__version__ = '1.0.1'
__email__   = 'jonfisik@hotmail.com'
__date__    = '08/05/2021'
'''
Qualquer número natural de quatro algarismos pode ser dividido
em duas dezenas formadas pelos seus dois primeiros e dois 
últimos dígitos.

Exemplos:
1297: 12 e 97
5314: 53 e 14

Escreva um programa que imprime todos os milhares (4 algarismos), 1000 <= n < 10000, cuja raiz quadrada seja a soma das dezenas formadas pela divisão acima.
        Exemplo: raiz de 9801 = 99 = 98 + 01
        Portanto 9801 é um dos números a ser impresso.
'''
#   1000 --> 10  00 --> 10 + 00 = 10 --> 10**2 = 100 == 1000 [V/F] imprimir 1000
#   1001 --> 10  01 --> 10 + 01 = 11 --> 11**2 = 121 == 1001 [V/F] imprimir 1001  
#   .
#   .
#   .
#   9801 --> 98  01 --> 98 + 01 = 99 --> 99**2 = 9801 == 9801 [V/F] imprimir 9801
#--------------------------------------------

def traco():
    return print('-----'*10)

print('')
print("TESTE MILHARES 1000 - 10 000")
traco()

# váriaveis 
num = 1000

while num < 10000:
    aux = num
    dois_ultm = aux%100

    aux //= 100

    dois_prim = aux%100

    if (dois_ultm + dois_prim)**2 == num:
        print(f'>>> {num}')

    num += 1

traco()
print('')
# END