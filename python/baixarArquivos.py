import os
import requests

def baixarArquivo(url, endereco):
    # faz requisição ao servidor - guardar em uma variável
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
            print('Donwload finalizado Salvo em: {}'.format(endereco))
    else:
        resposta.raise_for_status()

if __name__=="__main__":
    BASE_URL = 'https://aprendafisica.com/gallery/aula%200{}%20-%20introdu%C3%A7%C3%A3o%20%C3%A0%20f%C3%ADsica.pdf'
    SAIDA = 'saida'
    for i in range(1,10):
        nomeArquivo = os.path.join(SAIDA, 'aula-{}.pdf'.format(i))
        baixarArquivo(BASE_URL.format(i), nomeArquivo)
