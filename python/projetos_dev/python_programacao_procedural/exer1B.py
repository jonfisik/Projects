'''
2 - Crie uma função que receba 3 números e exiba a soma entre eles
'''
def soma(x = 0, y = 0, z = 0):
    w = x + y + z
    return w


a = float(input('Digite um número a = '))
b = float(input('Digite um número b = '))
c = float(input('Digite um número c = '))

res = soma(a, b, c)

print(f'O resultado da soma de {a} + {b} + {c} = {res}')