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