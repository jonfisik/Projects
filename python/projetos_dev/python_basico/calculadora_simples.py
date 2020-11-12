'''
Calculadora simples
'''
def traco(valor = 5):
    print('-'*valor)


traco(30)
print('CALCULADORA SIMPLES - V1.0'.center(30))
traco(30)

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input(''' 
    [+] SOMA
    [-] DIFERENÇA
    [*] MULTIPLICAÇÃO
    [/] DIVISÃO
    Digite um operador: ''')
    if not num_1.isdecimal() or not num_2.isdecimal():
        print('Por favor, digite um valor numérico.')
        continue

    if operador in '+-*/':
        num_1 = float(num_1)
        num_2 = float(num_2)
        # + - / *
        if operador == '+':
            print('>>', num_1 + num_2)
        elif operador == '-':
            print('>>', num_1 - num_2)
        elif operador == '*':
            print('>>', num_1 * num_2)
        elif operador == '/':
            print('>>', num_1 / num_2)
    else:
        print('Por favor, escolha o operador correto.')




    sair = input('Deseja sair [S/N] - ')

    traco(30)
    if sair in 'Ss':
        print('Finalizando calculadora...')
        break
    traco(30)