"""
Faça uma lista de tarefa com as seguintes opções:
    adiconar tarefas
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)

Solução com outras funções.
"""
# Funções
def mostrarLista(funcao):
    for valores in funcao:
        print(f'\033[1,32m - {valores}')

def adicionarTarefa():
    txt = input('\033[mDigite o item que deseja adicionar a lista: ').strip().title()
    lista.append(txt)
    return lista

def desfazer(lista):
    temporario.append(lista[-1])
    lista.pop()
    return lista

# Listas
lista = []
temporario = []

# programa
while True:
    print('\033[1m - Menu de opções -')
    print('\033[m1 - Adicionar Item\n'
                '2 - Mostrar Itens\n'
                '3 - Desfazer\n'
                '4 - Refazer\n'
                '5 - Sair / Gerar Lista')
    while True:
        while True:
            try:
                acao = input('\033[1;33mDigite uma das opções a cima: \033[m')
                acao = int(acao)
            except:
                print('Digite apenas números.')
                pass
        if acao > 5:
            print('O numero digitado não corresponde a nenhuma opção.')
        elif acao < 1:
            print('O número digitado não corresponde a nenhuma opção.')
        else:
            break
    if acao == 1:
        adicionarTarefa()
    elif acao == 2:
        print(f'\033[m{" "}', end='')
        print(f'\033[1m-='*20)
        print(f'\033[1;32 {"<<<LISTA>>>": ^40}')
        mostrarLista(lista)
        print(f'\033[m{" "}', end='')
        print('\033[1m-='*20)
    elif acao == 3:
        try:
            desfazer(lista)
        except:
            print('\033[1;31mNão há itens para desfazer'
                  '\nPor favor digite novamente!\033[m')
            pass
    elif acao == 4:
        try:
            lista.append(temporario[len(temporario)-1])
            temporario.pop()
        except:
            print('\033[1;31mNão há itens para refazer'
                  '\nPor favor digite novamente!\033[m')
            pass
    elif acao == 5:
        nome = input('Digite o nome do arquivo do arquivo para gerar sua lista (max 5 caracteres): ')[:6]
        nome += '.txt'
        titulo = input('Digite um título para sua lista: ').upper
        break
with open(nome, 'a+') as file:
    file.write(f'{titulo}\n')
    for itens in lista:
        file.write(f'{itens}\n')
    file.close
print('Obrigado por consultar a lista!')