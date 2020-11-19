'''
Sistema de perguntas e respostas.
'''
def traco(n=30):
    return print('-' * n)


traco()
print('JOGO DAS PERGUNTAS V1.0'.center(30))
traco()
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '3',
            'd': '2'
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 x 2? ',
        'respostas': {
            'a': '4',
            'b': '2',
            'c': '6',
            'd': '8'
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 10 / 2? ',
        'respostas': {
            'a': '4',
            'b': '2',
            'c': '6',
            'd': '5'
        },
        'resposta_certa': 'd',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 10 x 2? ',
        'respostas': {
            'a': '20',
            'b': '2',
            'c': '6',
            'd': '8'
        },
        'resposta_certa': 'a',
    },
}
respostas_certas = 0
for key_p, value_p in perguntas.items():
    print(f'{key_p}: {value_p["pergunta"]}')

    #print('Respostas: ')
    for key_r, value_r in value_p['respostas'].items():
        print(f'[{key_r}]: {value_r}')

    resposta_usuario = input('Sua respostas: ')
    if resposta_usuario == value_p['resposta_certa']:
        print('Eeehhh! Você acertou!!!')
        respostas_certas += 1
    else:
        print('Vixe! Você errou!!')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = (respostas_certas / qtd_perguntas) * 100

print(f'Você acertou {respostas_certas} reposta(s).')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto} %')