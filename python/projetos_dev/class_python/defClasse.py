__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '28/06/2021'
'''
Definição classe
Especificação (conj. de regras) de um objeto. Objeto é a instância (personificação) de uma classe.
'''
# Funções
def traco(n=5):
    print('---'*n)
    return

class Carro:
    valMax = 0
    ligado = False
    cor = ""

carro1 = Carro()
carro2 = Carro()

carro1.valMax = 200
carro1.cor = "Preto"
carro1.ligado = False

print('Classe V1.0.0')
traco()
print(f'Vel. Máx: {carro1.valMax}')
print(f'Cor: {carro1.cor}')
print(f'Ligado: {carro1.ligado}')
estado = 'Sim' if carro1.ligado else 'Não'
print(f'Ligado: {estado}')
traco()



#END
