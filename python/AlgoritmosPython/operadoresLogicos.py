__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '27/12/2021'
'''
Operadores lógicos -  AND, OR e NOT
'''

def traco():
    return print('-----'*10)

print('')
print("OPERADORES AND & OR - ")
traco()

operador = str(input('''
    [A] - AND
    [B] - OR
    Escolha o operador - '''))
print('')

if operador == 'A' or operador == 'a':
    print('Operador AND.')
    binario1 = int(input('Digite 0 ou 1: '))
    binario2 = int(input('Digite 0 ou 1: '))

    if binario1 == 1 and binario2 == 1:
        resultado = 'V'
        print(f'{resultado} - verdadeiro.')
    else:
        resultado = 'F'
        print(f'{resultado} - falso.')
elif operador == 'B' or operador == 'b':
    print('Operador OR.')
    binario1 = int(input('Digite 0 ou 1: '))
    binario2 = int(input('Digite 0 ou 1: '))

    if binario1 == 0 or binario2 == 0:
        resultado = 'V'
        print(f'{resultado} - verdadeiro.')
    else:
        resultado = 'F'
        print(f'{resultado} - falso.')
traco()