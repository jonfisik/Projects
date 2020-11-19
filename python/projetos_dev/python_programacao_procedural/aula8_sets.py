# add, update, clear, discard
# union | une
# instersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois set, mas não em ambos)
#
def traco(n=30):
    return print('-'*n)


# exemplos de criação de set
# recebe apenas valores - não tem índices
traco()
set1 = {1, 2, 3, 4, 5}
print(set1)
traco()

# pode-se apenas iterar os elementos
for i in set1:
    print(i)
traco()

# outra forma de criar set
set2 = set()
# add elementos
set2.add(3)
set2.add(5)
set2.add('jona')
print(set2)
set2.discard(3)
print(set2)
traco()
# função update - itera sobre cada elemento da string
# set - não respeitam ordem
set2.update('Python')
# não eceitam elementos duplicados
set2.update('thyA')
print(set2)
traco()
lista = [1, 2, 3, 6, 6, 7, 8, 9, 9, 'jona', 'jonatan', 'jona']
lista = set(lista)
lista = list(lista)
print(lista)
traco()

# unir sets
set3 = set1 | set2
print(set3)

# intercecção entre sets
set4 = set1 & set2
print(set4)

# diferença entre sets
set5 = set1 - set2
print(set5)
set5 = set2 - set1
print(set5)

# simétrico
set6 = set1 ^ set2
print(set6)