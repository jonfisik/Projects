'''
Desempacotamento de lista
'''
lista = ['Luiz', 'João', 'Maria',0,1,2,3,4,5,6,7,8,9,100]
n1, n2, n3, *outra_lista, ultimo_da_lista = lista
# n1, n2, *_ = lista # não será usado os outros valores
print(n1, n2, n3, outra_lista)
print(outra_lista)
print(outra_lista[5])
print(ultimo_da_lista)