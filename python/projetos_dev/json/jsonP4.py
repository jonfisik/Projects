__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física & Matemática'
__date__    = '23/12/2021'
'''
Manipulando json
'''
import json
{
    'nome':'Bruno',
    'time':'aviadores',
    'vivo':'True',
    'energia':'1000',
    'mochila':['pederneira','corda','linha','arame'],
    'aeronaves':[
        {'tipo':'transporte','habilidade':800},
        {'tipo':'ataque','habilidade':1000},
        {'tipo':'reconhecimento','habilidade':50}
    ]
}

jogador_j = '{"nome":"Bruno","time":"aviadores","vivo":"True","energia":"1000","mochila":["pederneira","corda","linha","arame"],"aeronaves":[{"tipo":"transporte","habilidade":800},{"tipo":"ataque","habilidade":1000},{"tipo":"reconhecimento","habilidade":50}]}'

#
## Converter json em elemento do python em formato de string(loads)
#
jogador = json.loads(jogador_j)

# chaves
for c in jogador:
    print(f'- {c}: ')
print('')

# items
for i in jogador.items():
    print(f'- {i}: ')
print('')

# valores
for v in jogador.values():
    print(f'- {v}: ')
print('')

# nome do jogador, time etc. chaves
print(jogador["nome"])
print(jogador["energia"])
print(jogador["aeronaves"])
print('')

# items da mochila
for im in jogador["mochila"]:
    print(im)
print('')

for a in jogador["aeronaves"]:
    print(a)