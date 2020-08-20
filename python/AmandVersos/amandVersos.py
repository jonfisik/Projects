from time import sleep
from os import system
print('-='*30)
print(f'{"RECADOS DO CORAÇÃO":^60}')
print('-='*30)
nome = str(input('Qual o nome do seu amigo? '))
print('--'*30)
tema = 0
while tema!= 5:
    print('''
    [1] BÍBLICO
    [2] AMOR
    [3] MOTIVACIONAL
    [4] AMIZADE
    [5] SAIR DO PROGRAMA
    ''')
    tema = int(input('>>>>> Qual tema você escolhe? '))
    print('-'*60)
    if tema == 1:
        frase = 0
        while frase != 5:
            print('''
            [1] - lalalala
            [2] - abababababababbabab
            [3] - papapapapapapapapap
            [4] - mamamamamammamamama
            [5] - tatatattatattatatta.''')
            
            frase = int(input('>>>>> Escolha uma frase para seu irmão(ã). '))
            print('--'*30)
            if frase == 1:
                print(f'''
                >>> {nome} 
                lalalala.''')
            elif frase == 2:
                print(f'''
                >>> {nome} 
                abababababababbabab.''')
            elif frase == 3:
                print(f'{nome} papapapapapapapapap.')
            elif frase == 4:
                print(f'{nome} mamamamamammamamama.')
            elif frase == 5:
                print('Saindo de frase.')
                break
            else:
                print('Tente novamente')    
    elif tema == 2:
        print('Escolha uma frase para seu amor.')
    elif tema == 3:
        print('Escolha uma frase para seu amigo.')
    elif tema == 4:
        print('Escolha uma frase para seu amigo.')
    elif tema == 5:
        print(f'{"Finalizando programa...":^60}')
        sleep(2)
        print(f'{"Obrigado. Volte sempre!":^60}')
        print('-='*30)
    else:
        print('Opção inválida. Tente Novamente!')
