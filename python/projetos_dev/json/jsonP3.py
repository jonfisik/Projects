__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '23/12/2021'
'''
Passando para json
'''
import json

#
##
#
carros_dictionary = {
    'marca': 'honda',
    'modelo': 'HRV',
    'cor': 'prata'
}
# dictionary -> objeto json

carros_list = ['honda','volkswagem','ford','fiat','chevrolet']
# list -> array json

carros_tuplas = ('honda','volkswagem','ford','fiat','chevrolet')
# tupla -> array json

print('')
carros_j = json.dumps(carros_dictionary)
print(carros_j)
print('')
carros_j = json.dumps(carros_tuplas)
print(carros_j)
print('')
carros_j = json.dumps(carros_list)
print(carros_j)
print('')
# indent: identa o dicionário, separators: troca os separadores, sort_keys=True: ordena em ordem crescente 
carros_j = json.dumps(carros_dictionary,indent=6,separators=(': ', ' = '),sort_keys=True)
print(carros_j)
print('')