__author__  = 'JPaschoal'
__version__ = '1.0.1'
__email__   = 'jonfisik@hotmail.com'
__date__    = '04/05/2021'
#
# Atalho contador - 
#
'''
cont operação=
+=, -=, *=, /=, //=, %=
>>> cont = 0

>>> cont = cont + 1
>>> cont += 1

>>> cont = cont * 2
>>> cont *= 2
------------------------------------------
Dizemos que um número natural é triangular se ele é produto de três númeors
naturais consecutivos
Exemplo
120 -- 4.5.6 == 120
Dado um número não negativo n, verificar se n é triangular.
'''
def traco():
    return print('----'*10)

print('')
print("TESTE - NÚMERO TRIANGULAR")
traco()
numero = int(input("Digite um número: "))

i, j, k = 1, 2, 3
# i = 1 -- i*(i+1)*(i+2) forma alternativa
while i * j * k < numero:
    i += 1
    j += 1
    k += 1
    print(f'- {i} x {j} x {k} = {i*j*k}')
print('')
if i * j * k == numero:
    print(f'- {i} x {j} x {k} = {numero}.')
    print(numero, 'é triangular.')
else:
    print(numero, 'não é triangular.')

traco()
print('Fim teste.')
print('')
# END 