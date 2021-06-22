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
            [sg.Text('Nome',size=(7,0)),sg.Input(size=(25,0),key='nome')],
            [sg.Text('Endereço',size=(7,0)),sg.Input(size=(25,0),key='endereco')],
            [sg.Text('Número',size=(7,0)),sg.Input(size=(6,0), key='num'),sg.Text('CEP',size=(4,0)),sg.Input(size=(10,0),key='cep')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','cartoes',key='aceitaCartao'),sg.Radio('Não','cartoes',key='naoAceitaCartao')],
            [sg.Slider(range=(0,225), default_value=0, orientation='h',size=(15,20),key='sliderVelocidade')],
            # sg.Button - cria o botão
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        # Janela
        self.janela = sg.Window('Dados do usuário').layout(layout)
#   def Iniciar(self):
#        print(self.values)

    def Iniciar(self):
        while True:
             # Extrair dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            endereco = self.values['endereco']
            num = self.values['num']
            cep = self.values['cep']
            aceita_gmail = self.values['gmail']
            aceita_outlook =self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'endereco: {endereco}')
            print(f'numero: {num}')
            print(f'cep: {cep}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_cartao}')
            print(f'aceita cartao: {aceita_cartao}')
            print(f'nao aceita cartao: {nao_aceita_cartao}')
            print(f'velocidade script {velocidade_script}')


# Instanciando classe
tela = TelaPython()
tela.Iniciar()


