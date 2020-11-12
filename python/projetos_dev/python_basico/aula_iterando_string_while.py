'''
Iterando strings - while
'''
#        Índices
#        0123456789.......................33 << Iterável
frase = 'O rato roeu a roupa do rei de Roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase: # iteração, iterar
    print(f'Índice[{contador}] >> {frase[contador]}')
    nova_string += frase[contador]
    contador += 1
    print(nova_string)
print('-'*20)

frase = 'O rato roeu a roupa do rei de Roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador += 1
print(nova_string)

print('-'*20)

frase = 'O rato roeu a roupa do rei de Roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_usuario = input('Qual letra deseja colacar para Maiúscula? ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
