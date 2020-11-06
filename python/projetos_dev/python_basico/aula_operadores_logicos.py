'''
Operadores lógicos
and, or, not, in, e not in
'''
print('-'*45)
print('COMPARANDO Versão 1.0'.center(45))
print('-'*45)
print('OPERADORES LÓGICOS'.center(45))
print('-'*45)
print('Para acessar o sistema faça seu LOGIN.')
print('-'*45)
nome1 = 'Jonatan'
senha1 = 12345678
nome = str(input('Digite seu login: ')).split()
senha = int(input('Digite sua senha: '))
print('-'*45)

valor = (nome1 == nome or senha1 == senha)
login = True
if login == valor:
    print('Logado...'.center(45))
else:
    print('ERRO de login.'.center(45))
    print('SAINDO DO SISTEMA.'.center(45))
    print('-' * 45)
    exit()

print('-'*45)
opcao = str(input('''[A] Caracter
[B] Número
Escolha a opção: '''))
print('-'*45)
if opcao in 'Aa':
    letra1 = input('Digite a 1° caracter: ')
    letra2 = input('Digite a 2° caracter: ')
    print('-'*45)
    if letra1 == letra2:
        print(f'[{letra1}] é igual a [{letra2}]'.center(45))
    else:
        print(f'[{letra1}] é diferente de [{letra2}]'.center(45))
elif opcao in 'Bb':
    num1 = float(input('Digite o 1° número: '))
    num2 = float(input('Digite o 2° número: '))
    print('-' * 45)
    if num1 == num2:
        print(f'[{num1}] é igual a [{num2}]'.center(45))
    else:
        print(f'[{num1}] é diferente de [{num2}]'.center(45))
print('-'*45)
print('FIM DO PROGRAMA'.center(45))
print('-'*45)