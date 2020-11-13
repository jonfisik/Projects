'''
Joga da forca - palavra secreta
'''
def traco(valor = 30):
    print('-'*valor)

traco()
print('JOGO DA ADVINHAÇÃO v1.0'.center(30))
traco()
secreto = 'escrever'
digitado = []
chances = 3

while True:
    if chances <= 0:
        print(f'Você perdeu!!! A palavra secreta era {secreto.upper()}.')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhhh isso não vale, digite apenas uma letra.')
        continue

    digitado.append(letra)

    if letra in secreto:
        print(f'Uhuuuuuuuu, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Affff, a letra "{letra}" não existe na palavra secreta.')
        digitado.pop()
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitado:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'PARABÉNS Você ganhou!!! Acertou a palvras {secreto_temporario.upper()}.')
        traco()
        break
    else:
        print(f'A palavras secreta está assim {secreto_temporario}.')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chance(s).')
    traco()
    print()
