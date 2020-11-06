'''
    Tipos de dados
    str - string - textos 'Assim' ou "Assim"
    int - inteiro - 12345 0 -9 10 -11
    float - real/ponto flutuante 16.65 -10.6
    bool - booleano/lógico - True/False
'''
print('- Isaac', type('Luiz'))
print('-', 10, type(10))
print('-', 23.25, type(23.25))
print('-', 10==10, type(10==10))
print('-', 'L'=='l', type('L'=='l'))
# converter tipos
print('--'*15)
print('luiz', type('luiz'), bool('luiz')) # Para strings não vazias sempre retorna True
print('10', type('10'), ',', type(int('10')))