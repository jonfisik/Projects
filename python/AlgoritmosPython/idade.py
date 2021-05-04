__author__  = 'JPaschoal'
__version__ = '1.0.1'
__email__   = 'jonfisik@hotmail.com'
__date__    = '04/05/2021'

def traco():
    return print('-----'*10)

print('')
print("IDADE, QUANDO?")
traco()
numero = int(input('Digite o número de pessoas: '))
cont = 0
print('')
print('Informe')
while cont < numero:
    nome = str(input('Nome: '))
    dia = int(input('Dia de nascimento: '))
    mes = int(input('Mês de nascimento: '))
    ano = int(input('Ano de nascimento: '))
    idade = int(input('Idade a ser completada: '))

    print('')
    print(f'{nome}, você fará {idade} anos nos dia {dia}/{mes}/{ano + idade}.')
    cont += 1
    print('')

traco()
print('')
# END 