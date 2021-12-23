__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '23/12/2021'
'''
Transformando Dictionary em JSON.
'''
import json

carros = {
    "marca": "honda",
    "modelo": "HRV",
    "cor": "prata"
}

carros_json = json.dumps(carros)

print("")
print(carros_json)
print("")