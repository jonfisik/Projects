# Não se deve usar em argumentos de funções objetos mutáveis
# Mutavél: Listas, Dicionários.
# Imutáveis: Tuplas, strings, núemeros, True,False, none.

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista =[]
    lista.extend(clientes_iteravel)
    return lista

lista_de_clientes_1 = ['Fabricio']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_de_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas','Zico'])
clientes3 = lista_de_clientes(['Jonatan'])

print('---'*10)
print(clientes1)
print(clientes2)
print(clientes3)
print('---'*10)