'''
list comprehension - exercício
'''

string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

n = 10
# contadores
contadores = [i for i in range(0, len(string), n)]
print(contadores)
# mostra onde iniciam e onde terminam os intervalos
inicio_fim = [(i, i + n) for i in range(0, len(string), n)]
print(inicio_fim)
# mostra os elementos da "string" separados intervalos
lista = [string[i: i + n] for i in range(0, len(string), n)]
print(lista)
intervalo = [f'string[{i}: {i + n}]' for i in range(0, len(string), n)]
print(intervalo)
# juntar a lista com pontos >> .join <<
retorno = '.'.join(lista)
print(retorno)