__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '29/06/2021'
'''
Tratamento de Erro
'''
print('')
print('--'*10)

x = 10
try:
    print(x)
except:
    print('Erro no programa')
else:
    print('Tudo certo.')
finally:
    print('Fim do tratamento.')

print('--'*10)
print('')

num = -1
if num < 1:
    raise Exception('Valor não permitido.')

print('--'*10)
print('')