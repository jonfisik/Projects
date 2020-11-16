'''
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
'''
def saudacao(saud, nome):
    print(f'{saud}, {nome}.')

x = str(input('Digite uma saudação: '))
y = str(input('Digite um nome: '))
saudacao(x, y)

'''
2 - Crie uma função que receba 3 números e exiba a soma entre eles
'''
def soma(x = 0, y = 0, z = 0):
    w = x + y + z
    return w


a = float(input('Digite um número a = '))
b = float(input('Digite um número b = '))
c = float(input('Digite um número c = '))

print(soma(a, b, c))

'''
Crie uma função que receba 2 números. O primeiro é um valor e osegundo é um percentual. Retorne o valor o
valor do primeiro somado do aumento do percentual do mesmo. 
'''
def percentual(valor, porcento):
    total = valor + (valor * (porcento/100))
    return total


x = float(input('Digite um valor: '))
y = float(input('Qual o percentual a ser calculado? '))
percentual(x, y)

print(f'O total de {y}% de {x} é {percentual(x,y)}')