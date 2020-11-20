'''
list comprehension
'''
def traco(valor=30):
    return print('-'*valor)


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex2 = [variavel for variavel in lista1]
print(f'Lista 1 >> {lista1}')
print(f'Lista 2 >> {ex2}')
traco(40)
ex3 = [variavel*2 for variavel in lista1]
print(f'Lista 3 >> {ex3}')
traco(40)
ex4 = [(v, v2) for v in lista1 for v2 in range(3)]
print(f'Lista 4 >> {ex4}')
traco(40)
lista2 = ['Jona', 'Panto', 'Pasc']
ex5 = [v.replace('a','@').upper() for v in lista2]
print(ex5)
traco(40)
tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in tupla]
ex6 = dict(ex5)
print(ex5)
print(ex6)
print(ex6['valor2'][:])
traco(40)
lista3 = list(range(100))
ex6 = [v for v in lista3 if v % 10 == 0]
print(ex6)
ex7 = [v for v in lista3 if v % 3 == 0 if v % 10 == 0]
print(ex7)
ex8 = [v if v % 3 == 0 else f'{v} Não é divisível por 3' for v in lista3]
print(ex8)
ex9 = [v if v % 3 == 0 and v % 8 == 0 else f'{v} Não é divisível por 3 e 8' for v in lista3]
print(ex9)