'''
Quantidade de caracteres len() 07-11-2020
len() é igual ao método __len__()
'''
usuario = str(input('Digite seu usuário: '))
qtd_caracteres = len(usuario)

#print(f'Caracter(es) digitado(s) {qtd_caracteres} caracteres. Tipo da função len() {type(qtd_caracteres)}.')

if ' ' in usuario:
    print('Você digitou espaços em branco. Tente novamente.')
elif qtd_caracteres <= 7:
    print('Seu usuário precisa ter 8 ou mais caracteres.')
elif qtd_caracteres >= 8:
    print('Usuário cadastrado.')