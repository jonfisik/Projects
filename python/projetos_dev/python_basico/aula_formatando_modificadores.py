'''
Formatando valores com modificadores
:s - textos (strings)
:d Inteiros (int)
:f - Números de ponto flutuantes (float)
:.(NÚMEROS)f - quantidades de casas decimais (float)
:(CARACTER)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
> - esquerda
< - direita
^ - centro
'''
num_1 = 1
num_2 = 365
num_3 = 454
nome = 'jona'
nome_formatado = '{:-^10}'.format(nome)
val = 'OI'
val_formatado = '{v:-^5}{v:-^5}'.format(v=val)
sobrenome = 'paschoal'
nome_sobrenome_formatado = '{1:-^10}{0:-^10}'.format(nome, sobrenome)
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
print('-'*10)
print(f'{num_1:0>10}')
print(f'{num_2:0>10}')
print(f'{num_2:a>10}')
print(f'{num_2:x^10}')
print(f'{num_3:0>10.2f}')
print(f'{nome:#^10}')
print((10-len(nome))/2)
print(nome_formatado)
print(val_formatado)
print(f'{sobrenome:-^10}'.format(nome, sobrenome))
print(nome_sobrenome_formatado)
