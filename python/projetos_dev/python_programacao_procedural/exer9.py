"""
Faça uma lista de tarefa com as seguintes opções:
    adiconar tarefas
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)

"""
def show_op(fazer_lista):
    print()
    print('Tarefas: ')
    print(fazer_lista)
    print

def fazer_desfazer(fazer_lista, refazer_lista):
    if not fazer_lista:
        print('Nada a desfazer.')
        return
    
    ultimo_fazer = fazer_lista.pop()
    refazer_lista.append(ultimo_fazer)

def fazer_refazer(fazer_lista, refazer_lista):
    if not refazer_lista:
        print('Nada a refazer.')
        return

    ultimo_refazer = refazer_lista.pop()
    fazer_lista.append(ultimo_refazer)

def fazer_add(fazer, fazer_lista):
    fazer_lista.append(fazer)


if __name__=='__main__':
    fazer_lista = []
    refazer_lista = []

    while True:
        print()
        print('-----'*15)
        print('Funçoes [Desfazer (undo), Refazer (redo), listar (ls)]')
        fazer = input('Digite uma tarefa ou um comando: ')

        if fazer == 'ls':
            show_op(fazer_lista)
            continue
        elif fazer == 'undo': # undo - desfazer
            fazer_desfazer(fazer_lista, refazer_lista)
            continue
        elif fazer == 'redo': #undo - refazer
            fazer_refazer(fazer_lista, refazer_lista)
            continue

        fazer_add(fazer, fazer_lista)

        

