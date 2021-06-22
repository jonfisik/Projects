__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '20/06/2021'

import PySimpleGUI as sg

# Classe
class TelaPython:
    def __init__(self):
        # Layout
        layout =[
            # sg.Text - cria a label, sg.Imput - recebe os dados
            [sg.Text('Nome'),sg.Input()],
            [sg.Text('Idade'),sg.Input()],
            [sg.Text('Endereço'),sg.Input()],
            # sg.Button - cria o botão
            [sg.Button('Enviar Dados')]
        ]
        # Janela
        janela = sg.Window('Dados do usuário').layout(layout)
        # Extrair dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

# Instanciando classe
tela = TelaPython()
tela.Iniciar()


