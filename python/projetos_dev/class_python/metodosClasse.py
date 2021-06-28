__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '28/06/2021'
'''
Métodos em classe
Método --> Função
Construtor é um método chamado quando a classe é instanciada.
'''
# Funções
def traco(n=8):
    print('---'*n)
    return

class Carro:
    valMax = 0
    ligado = False
    cor = ""
    # def __init__(self referência para própria classe, parâmetros de entrada - o que o método irá fazer):
    def __init__(self, vel, lig, c):
        self.velMax = vel
        self.ligado = lig
        self.cor = c
    
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def andar(self):
        if(self.ligado):
            print('Andando.')
        else:
            print('Carro desligado.')

    def mostrar(self):
        print(f'Velocidade Máx: {self.velMax}')
        print(f'Cor...........: {self.cor}')
        estado = 'Sim' if self.ligado else 'Não'
        print(f'Ligado........: {estado}')
        traco()

#
#Instanciado a classe carro
#         

carro1 = Carro(200,False,"Preto")
carro2 = Carro(350,False,"Branco")

# main()
print('')
traco()
print('Método construtor V1.0.0')
traco()

carro1.ligar()

carro1.mostrar()
carro2.mostrar()


carro1.andar()
carro2.andar()

traco()
print('')


#END
