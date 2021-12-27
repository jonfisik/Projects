__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '27/12/2021'
'''
Operadores lógicos -  AND, OR e NOT
'''

operador = str(input('''
    [A] - AND
    [B] - OR
    Escolha os operador - '''))

if operador == 'A' or operador == 'a':
    binario1 = int(input('Digite 0 ou 1: '))
    binario2 = int(input('Digite 0 ou 1: '))

    if binario1 == 1 and binario2 == 1:
        resultado = 'V'
        print(f'{resultado} - verdadeiro.')
    else:
        resultado = 'F'
        print(f'{resultado} - falso.')
elif operador == 'B' or operador == 'b':
    binario1 = int(input('Digite 0 ou 1: '))
    binario2 = int(input('Digite 0 ou 1: '))

    if binario1 == 0 and binario2 == 0:
        resultado = 'F'
        print(f'{resultado} - falso.')
    else:
        resultado = 'V'
        print(f'{resultado} - verdadeiro.')
