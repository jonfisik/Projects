__author__  = 'JPaschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Criando Classes'
__date__    = '08/06/2021'

#-----------------------------------------------------------
def traco():
    return print('-----'*10)

# Class
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    #pass
    def Ligar(self):
        print('Ligando PC')
    
    def Desligar(self):
        print('Desligando PC')
    
    def ExibirImformacoesDestePC(self):
        print(self.marca,self.memoria_ram, self.placa_de_video)

print('')
print("Classe Computador - ")
traco()
Computador1 = Computador('Asus','16gb','Nvidia')
Computador1.Ligar()
Computador1.Desligar()
Computador1.ExibirImformacoesDestePC()

traco()
print('')
# END