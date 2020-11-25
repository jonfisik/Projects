'''
Agrupar elementos
Groupby
'''
from itertools import groupby,tee

# lista com dicionários
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Zé', 'nota': 'C'},
    {'nome': 'João', 'nota': 'D'},
    {'nome': 'Tiago', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Judas', 'nota': 'B'},
    {'nome': 'Bartolemeu', 'nota': 'A'},
    {'nome': 'Nadson', 'nota': 'C'},
    {'nome': 'Gustavo', 'nota': 'A'},
    {'nome': 'Gerônimo', 'nota': 'B'},
    {'nome': 'Zaqueu', 'nota': 'D'},
    {'nome': 'Márcio', 'nota': 'A'},
]

# visualizar a lista ordenada pelas notas
alunos.sort(key=lambda item: item['nota'])

for aluno in alunos:
    print(aluno)
print()

# agrupando os dados da lista
# alunos_agrupados = groupby(alunos, lambda item: item['nota'])
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
    print()
    # quantidade = len(list(valores_agrupados))
    # print(f'{quantidade} alunos tiraram a nota {agrupamento}')
#------------------------------------------------------------------
print('-'*30)
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    copia1, copia2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in copia1:
        print(f'\t{aluno}')

    quantidade = len(list(copia2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()
