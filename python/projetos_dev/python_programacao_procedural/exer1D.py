'''
4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, se o parâmentro da função
for divisível por 5 retorne por 5,retorne buzz. Se o parâmetro da função for divisíel por 5 e por 3, retorne FizzBizz,
caso contrário retorne o número enviado.    
'''
def divisor(valor):
    if (valor % 5 == 0) and (valor % 3 == 0):
        resp = 'FizzBuzz'
    elif valor % 3 == 0:
        resp = 'Fizz'
    elif valor % 5 == 0:
        resp = 'BUzz'
    else:
        resp = valor

    return resp

while True:
    numero = int(input('Digite um número inteiro: '))
    print(divisor(numero))
    x = input('Quer continuar: [S/N]').upper()
    if x in 'N':
        print('Fim programa.')
        break