'''
Trocando valores entre variáveis
'''

x = 10
y = 'Luiz'
# forma tradicional
z = x
x = y
y = z
print(f'x = {x} e y = {y}')
# com python
x, y = y, x
print(f'x = {x} e y = {y}')
z = 'Teste'
x, y, z = z, x, y
print(f'x = {x}, y = {y} e z = {z}')