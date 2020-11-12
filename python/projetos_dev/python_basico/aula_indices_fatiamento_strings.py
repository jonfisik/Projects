'''
Manipulando strings
* Strings índices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print,etc..
Essas funções podem ser usadas diretamente em cada tipo.
'''
# Cada elemento de uma string em python possui um índice positivo.
#       [012345678] -> começando em zero
texto = 'Python_s2'
print('>>',texto[2]) # elemento da psoição '2'
print('>>',texto[8])
# índices negativos
#       -[987654321]
#        'Python_s2'
print('>>',texto[-1])
print('>>',texto[-9])
print('-'*12)
nova_string = texto[2:6] # A última posição não é incluida
print('>>', nova_string)
nova_string = texto[:6]
print('>>', nova_string)
nova_string = texto[7:]
print('>>', nova_string)
nova_string = texto[-9:-3]
print('>>', nova_string)
nova_string = texto[-9::2]
print('>>', nova_string)
print('-'*12)
for texto in texto:
    print(texto)