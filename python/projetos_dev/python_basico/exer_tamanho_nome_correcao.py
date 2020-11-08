'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "seu nome é curto";
se tiver 5 ou 6 letras "seu nome é normal": maior que 6 "seu nome é muito grande".
'''
nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto.')
elif tamanho <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')