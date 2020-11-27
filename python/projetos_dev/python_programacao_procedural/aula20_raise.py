'''
raise
'''
## exemplo 1
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise
try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print(error)


## Exemplo 2 - própria msn de erro.
# def divide(a, b):
#     if b == 0:
#         raise ValueError('O denominador não pode ser zero.')
#     return a / b
#
# try:
#     print(divide(2,0))
# except ValueError as error:
#     print('Você está tentando dividir por ZERO!') # msn para o usuário
#     print('Log: ', error) # pode ser capturado em um arquivo de log
