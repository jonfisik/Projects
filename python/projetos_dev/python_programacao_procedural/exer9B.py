__author__  = 'Jonatan Paschoal - 25/04/2021'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - física'

#
# Listas
#
todo1 = []
undo1 = []
#
# Funções
#
def add(item, todolist):
    todolist.append(item)

def remove(item, todolist, undolist):
    if item in todolist:
        undolist.append(item)
        todolist.remove(item)
    else:
        print('Item não encontrado!')

def undo(todolist, undolist):
    try:
        todolist.append(undolist[-1])
        undolist.remove(undolist[-1])
    except IndexError:
        print('Não há nada para refazer.')
#
# Rotina principal
#
while True:
    print('###################LISTA DE TAREFAS###################')
    for i in todo1:
        print(i)
    print('###################LISTA DE TAREFAS###################')
    user_input = input('add remove undo\n')

    if user_input == 'add':
        user_add = input('Item a ser adicionado?\n->')
        add(user_add, todo1)
    if user_input == 'remove':
        user_remove = input('Item a ser removido?\n->')
        remove(user_remove, todo1, undo1)
    if user_input == 'undo':
        undo(todo1, undo1)