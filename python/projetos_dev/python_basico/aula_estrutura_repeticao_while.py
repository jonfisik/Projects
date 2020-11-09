'''
while em Python
Utilizado para realizar ações enquanto uma condição for verdadeira.
'''
x = 0
while x < 10:

    print(x)
    x = x + 1
print('FIM!')
print('-'*12)
y = 0
while y < 10:
    if y == 3:
        y = y + 1
        #continue
        #break
    print(y)
    y = y + 1
print('-'*12)

x = 0 # coluna

while x < 10:
    y = 0  # linha
    print(f'Para x = {x}')
    while y < 5:
        print(f'Coord. ({x}, {y})')
        y += 1
    x += 1
print('Acabou!')
print('-'*12)