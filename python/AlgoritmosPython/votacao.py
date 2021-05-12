__author__  = 'JPaschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__date__    = '12/05/2021'
'''
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''
#-----------------------------------------------------------

def traco():
    return print('-----'*10)

print('')
print("VOTAÇÃO - ")
traco()

#input
print("Iniciando votação...")
print('')
m = int(input('Digite o total de eleitores: '))
#-------------------------------------------------------------
voto = 0
nulo = 0
candA = candB = candC = 0

for i in range(1, m+1):
    print('''
            [1] Votar
            [2] Nulo
        ''')
    voto = int(input(f'Eleitor {i}. Escolha a opção >>> '))

    if voto == 1:
        print('''
            [A] Candidato A
            [B] Candidato B
            [C] Candidato C
        ''')
        votando = str(input('Escolha seu voto >>> '))
        
        if votando in 'aA':
            candA = candA + 1
        elif votando in 'bB':
            candB += 1
        elif votando in 'cC':
            candC += 1
    elif voto == 2:
        nulo += 1

# falta colocar porcentagem
print('')
print(f'Canditado A: {candA} - Canditado B: {candB} - Canditado C: {candC}')
print(f'Voto nulo: {nulo}')

traco()
print('')
# END