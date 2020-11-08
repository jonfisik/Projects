'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "seu nome é curto";
se tiver 5 ou 6 letras "seu nome é normal": maior que 6 "seu nome é muito grande".
'''

def traco():
    print('-'*50)


traco()
print('TAMANHO NOME v1.0'.center(50))
traco()

try:
    nome = str(input('Digite seu primeiro nome: ')).capitalize().strip()
    if nome.isnumeric():
        print('Teu nome é número?')
    elif not int(nome) == nome:
        print('Escreve esse nome direito.')
except:
    if nome == 'Jonatan':
        print('Esse nome é lindo!!!')
    elif 5 <= len(nome) <= 6:
        print(f'{nome}, seu nome é normalzinho. Dá pra o gasto.')
    elif len(nome) <= 4:
        print(f'{nome}, que nome curto. Teu pai é economista?')
    elif len(nome) > 6:
        print(f'Nossa {nome}, que exageiro de nome!')

traco()