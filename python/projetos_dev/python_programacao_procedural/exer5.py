'''
-> É uma lista de lista de números inteiros
-> As lista internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 eles podem ser duplicados

Exercício

-> Crie uma função que encontra o primeiros número duplicado considerando
 o segundo número como a duplicação.
    Requisitos:
    A ordem do número duplicado é considerada a partir da segunda ocorrencia (o número duplicado em si).
    ex: [1, 2, 3, ->3<-, 2, 1] 3
    Se não encontrar duplicados na lista, retorne -1.
'''

lista_de_listas_de_inteiros =[
    [4,7,1,2,3,6,9,5,8,10],
    [3,3,6,5,1,6,9,7,10,5],
    [8,9,5,1,3,6,10,10,8,7],
    [8,10,3,5,4,8,6,10,9,7],
    [1,6,5,3,2,9,7,8,8,5,],
    [10,5,6,3,2,9,7,4,3,5],
    [8,6,6,3,2,1,10,8,9,7],
]

def encontra_duplicado(parametro_lista):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in parametro_lista:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)

    return primeiro_duplicado

for lista_de_inteiro in lista_de_listas_de_inteiros:
    print(f'{lista_de_inteiro}, número duplicado {encontra_duplicado(lista_de_inteiro)}')