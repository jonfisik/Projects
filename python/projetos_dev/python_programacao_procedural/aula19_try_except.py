'''
try, except - tratamento de exceção
'''
# Exemplo de exceção e de como continuar o programa
try:
#    a = []
    print(a[1])
#    b = 1/0
except NameError as erro:
    print('Erro', erro)
except IndexError as erro:
    print('Erro índice.', erro)
except Exception as erro:
    print('Erro inesperado.')
#else: #se não houver erro, será executado
    print('Codigo executado com sucesso.')
finally: # executado sempre
    print('Executado sempre!')
print('O jogo continua.')