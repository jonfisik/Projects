'''
Validador CPF alternativo
'''
# Loop infinito
while True:
    #cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                             # Elimina os dois últimos digitos do CPF
    reverso = 10                                    # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                               # Primeiro índice vai de 0 a 9
            index -= 9                              # São os 9 primeiros dígitos do CPF

        total += int(novo_cpf[index]) * reverso     # Valor total da multiplicação

        reverso -= 1                                # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                               # Se o dígito for > que 9 o valor é 0
                d = 0
            total = 0                               # Zera o total
            novo_cpf += str(d)                      # Concatena o dígito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111111, 00000000000
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    #

    if cpf == novo_cpf and not sequencia:
        print('Válido.')
    else:
        print('Inválido.')

    resp = input('Quer continuar? [S/N] - ')
    if resp not in 'Ss':
        print('Volte sempre.')
        print('-'*15)
        break
    print('-'*15)
