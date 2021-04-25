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
            [1] - Bendiga ao Senhor a minha alma! Bendiga ao Senhor todo o meu ser! Bendiga ao Senhor a minha alma! Não esqueça de nenhuma de suas bênçãos!
            É ele que perdoa todos os seus pecados e cura todas as suas doenças, que resgata a sua vida da sepultura e o coroa de bondade e compaixão,
            que enche de bens a sua existência, de modo que a sua juventude se renova como a águia. O Senhor faz justiça e defende a causa dos oprimidos. Salmos 103:1-6
            
            [2] - Porque o Senhor é bom, e eterna a sua misericórdia; e a sua verdade dura de geração em geração. Salmos 100:5
            
            [3] - Porque nele vivemos, e nos movemos, e existimos. Atos 17:28
            
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
