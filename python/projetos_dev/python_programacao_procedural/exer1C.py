'''
3 - Crie uma função que receba 2 números. O primeiro é um valor e osegundo é um percentual. Retorne o valor o
valor do primeiro somado do aumento do percentual do mesmo.
'''
def percentual(valor, porcento):
    total = valor + (valor * (porcento/100))
    return total

def traco(x=10):
    print('--'*x)

traco(20)
x = float(input('Digite um valor: '))
y = float(input('Qual o percentual a ser calculado? '))
percentual(x, y)
traco(20)
print(f'A soma de {y}% com {x} é {percentual(x,y)}')
traco(20)