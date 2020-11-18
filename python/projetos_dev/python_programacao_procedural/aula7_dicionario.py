'''
Dicionários
'''
dicio = {'chave1': 'valor da chave'}
print(dicio)
dicio['chave2'] = 'Valor da nova chave'
print(dicio)
print(dicio['chave1'])
print('-'*20)
dicio1 = dict(ch = 'valor0', ch1 = 'valor1', ch2 = 'valor2')

print(dicio1)

print('-'*20)
# as chaves podem ser de qualquer natureza
dicio2 = {'str': '>> texto', 123: '>> chave como int', (1,2,3,): '>> chave como tupla'}

print(dicio2)

print(dicio2[(1,2,3)])

print(dicio2.get('chave não existe')) # verificar se chave existe

dicio2.update({'nova_chave': 'valor da nova chave'})

print(dicio2)

del dicio2['nova_chave']

print(dicio2)
print('-'*20)
# testando chaves e valores de chaves
print('str' in dicio2)
print('str' in dicio2.keys())
print('valor' in dicio2.values())
print(len(dicio2))
print('-'*20)

dicio3 = {'0 >>': 'valor 0', '1 >>': 'valor 1', '2 >>': 'valor 2'}
for k in dicio3:
    print(k)

for v in dicio3.values():
    print(v)

for k in dicio3.items():
    print(k[0], k[1])

for k, v in dicio3.items():
    print(k,v)

print('-'*20)
# dicionário dentro de dicionários
cliente = {
    'cliente1': {
        'nome': 'luiz',
        'sobrenome': 'otavio',
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'moreira',
    },
    'cliente3': {
        'nome': 'ze',
        'sobrenome': 'silva',
    },
}
# iteração para dicionários dentro de dicionários
for clientes_k, clientes_v in cliente.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

print('-'*20)
copia_rasa = cliente.copy()
print(copia_rasa)
import copy
# cria dicionaŕios independentes
copia_profunda = copy.deepcopy(cliente)
print(copia_profunda)
copia_profunda['cliente1']= 'teste'
print(copia_profunda)
copia_profunda['cliente2'][2]= 'teste'
print(copia_profunda)