'''
for in em python
Iterando strings com python
função range(start = 0, stop = 0, step = 1)
'''

# revisando while
texto = 'Python'
c = 0
while c < len(texto):
    print(texto[c])
    c += 1

print('-'*15)
texto = 'Python'
for letra in texto:
    print(letra)

print('-'*15)
texto = 'Python'
for n, letra in enumerate(texto):
    print(n, letra)

print('-'*15)
for n in range(5, 51, 2):
    print(n)

print('-'*15)
for n in range(50):
    if n % 5 == 0:
        print(n)

print('-'*15)
# continue - pula para o próximo laço
# break - termina o laço
texto = 'Python, Python'
nova_string = ''
for letra in texto:
    if letra == 't':
        #continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        #break
    else:
        nova_string += letra
print(nova_string)