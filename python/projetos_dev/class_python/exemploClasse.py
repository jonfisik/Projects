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

print('')
print("Classe computadores - ")
traco()
#-----------------------------------------------------------
Computador1 = Computador('Asus','8gb','Nvidia')
Computador2 = Computador('Dell','10gb','Gforce')
Computador3 = Computador('Acer','16gb','ATM')
#-----------------------------------------------------------
print(f'Computador 1 - {Computador1.marca,Computador1.memoria_ram,Computador1.placa_de_video}')
print(f'Computador 2 - {Computador2.marca,Computador2.memoria_ram,Computador2.placa_de_video}')
print(f'Computador 3 - {Computador3.marca,Computador3.memoria_ram,Computador3.placa_de_video}')
traco()
print('')
# END