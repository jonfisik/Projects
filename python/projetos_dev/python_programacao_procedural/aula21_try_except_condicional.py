'''
try, except com condicional
'''
def converte_numero(valor, fator):
    try:
        valor = int(valor)
        fator = int(fator)
        return valor * fator
    except ValueError:
        try:
            valor = float(valor)
            fator = float(fator)
            return valor * fator
        except ValueError:
            return 'Isso não é um número.'

while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Por quanto quer multiplicar? ')
    #converte_numero(numero1, numero2)
    if numero1 and numero2 is not None:
        print(f'{numero1} x {numero2} = {converte_numero(numero1,numero2)}')
        while True:
            resp = input('Quer continuar? [S/N] - ')
            if resp not in 'NnSs':
                print('Opção inválida.')
            elif resp in 'Ss':
                continue
            else:
            # elif resp in 'Nn':
            #     print('Finalizando programa.')
                break