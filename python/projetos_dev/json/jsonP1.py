__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '23/12/2021'
'''
Manipulando json como um dictionary.
'''
import json

carros_json = '{"marca": "honda", "modelo": "HRV", "cor": "prata"}'

carros = json.loads(carros_json)
print("")
print(carros)
print("")
print(carros["modelo"])
print("")

for x in carros.items():
    print("-------")
    print(x)

for k, v in carros.items():
    print("-------")
    print(k,v)

for x in carros:
    print("-------")
    print(x)

for x in carros.values():
    print("-------")
    print(x)