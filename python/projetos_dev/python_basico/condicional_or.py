'''
Operador or
'''
nome = input('Qual seu nome? ')
if nome:
    print(nome)
else:
    print('Você não digitou nada =(')
#--------------------------------------
nome = input('Qual seu nome? ')
print(nome or 'Você não digitou nada!')
