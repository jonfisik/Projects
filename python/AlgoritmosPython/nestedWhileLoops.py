n = int(input('Digite o número de empresas: '))
m = int(input('Digite o número de meses: '))

empresa = 1
print("")
while empresa <= n:
    mes = 1
    balanca = 0
    print('Empresa', empresa, ":")
    while mes <= m:
        print('Mês', mes,":")
        ganho = int(input('Digite o ganho da empresa no mês: '))
        gasto = int(input('Digite o gasto da empresa no mês: '))
        balanca = balanca + (ganho - gasto)
        print("")
        mes = mes + 1

    if balanca == 0:
        print('A empresa ', empresa,'ficou indiferente (balança = 0)')
    elif balanca > 0:
        print('A empresa ', empresa,'fechou com lucro de R$', balanca)
    else:
        print('A empresa ', empresa,'fechou com déficit de R$', balanca)
    empresa = empresa + 1
    print("")