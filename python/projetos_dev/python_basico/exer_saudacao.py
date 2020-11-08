'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Bom dia 0 - 11, Boa tarde 12 - 17 e Boa noite 18 - 23
'''
def traco():
    print('-'*50)


traco()
print('SAUDAÇÕES'.center(50))
traco()
try:
    hora = int(input('Olá, quantas horas marcam em seu relógio? '))
    minutos = int(input('Quantos minutos? '))
    traco()

    if (0 <= hora < 12) and (0 <= minutos <= 59):
        print(f'{hora} h e {minutos} min. Bom dia para você.')
    elif (0 <= hora < 11) and (minutos == 60):
        print(f'Caríssimo, já são {(hora + 1)} h. Bom dia.')
    elif (hora == 11) and (minutos == 60):
            print('Caríssimo, já estamos em nova tarde. Boa tarde.')


    if (12 <= hora < 18) and (0 <= minutos <= 59):
        print(f'{hora} h e {minutos} min. Boa tarde para você.')
    elif (12 <= hora < 17) and (minutos == 60):
        print(f'Caríssimo, já são {(hora + 1)} h. Boa tarde.')
    elif (hora == 17) and (minutos == 60):
            print('Caríssimo, já estamos em uma nova noite. Boa noite.')


    if (18 <= hora < 24) and (0 <= minutos <= 59):
        print(f'{hora} h e {minutos} min. Boa noite para você.')
    elif (18 <= hora < 23) and (minutos == 60):
        print(f'Caríssimo, já são {(hora + 1)} h. Boa noite.')
    elif (hora == 23) and (minutos == 60):
        print('Caríssimo, já estamos em um novo dia. Bom dia.')

    traco()
except:
    traco()
    print('ERRO! Esse não é um valor correto de tempo.')
    traco()