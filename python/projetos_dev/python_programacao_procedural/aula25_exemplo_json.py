import json
d1 = {
    'Pessoa1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa2': {
        'nome': 'Jona',
        'idade': 39,
    },
}

d1_json = json.dumps(d1, indent = True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)