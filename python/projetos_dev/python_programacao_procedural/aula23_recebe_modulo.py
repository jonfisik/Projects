import aula23_modulo

print(f'Pí = {aula23_modulo.PI}')

lista = [2, 4]
print(f'Lista >> {lista}')
print(f'{lista[0]} x {lista[1]} = {aula23_modulo.multiplica(lista)}')

from aula23_modulo import dobra_lista

print(f'Lista dobrada >> {dobra_lista(lista)}')