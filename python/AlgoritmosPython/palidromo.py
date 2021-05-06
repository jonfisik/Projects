__author__  = 'JPaschoal'
__version__ = '1.0.1'
__email__   = 'jonfisik@hotmail.com'
__date__    = '06/05/2021'
'''
Dizemos que um número natural n é palídromo (3) se
    o 1º algarismo é igual ao seu último algarismo,
    o 2º algarismo é igual ao seu penúltimo algarismo, 
    e assim sucessivamente.

Exemplos - 
Palídromos: 567765 e 32423.
Não palídromos: 567675.
Dado um número natural n > 10, verificar se n é palídrome.

'''
#   aux      dig     reverso     n
#   567765    0         0      567765
#-------------------------------------------
#   567765    5        5
#   56776     6        56--> 50 + 6 = 56
#   5677      7        567--> 560 + 7 = 567
#   567       7        5677--> 5670 + 7 = 5677
#   56        6        56776--> 56770 + 6 = 56776
#   5         5        567765--> 567760 + 5 = 567765
#   0
# aux//10   aux%10     reverso*10 + dig

# // divisão inteira
# % resto da divisão

def traco():
    return print('-----'*10)

print('')
print("PALÍDROMOS")
traco()

# input
n = int(input('Digite um número maior que 10: '))

# váriaveis 
aux = n
dig = reverso = 0

while aux != 0:
    dig = aux%10
    #print(f'{dig}')
    reverso = reverso*10 + dig
    #print(f'{reverso}')
    aux //= 10
    #print(f'{aux}')

print('')
if reverso == n:
    print(f'{n}, é palídromo.')
else:
    print('Não é palídrome.')
    
traco()
print('')
# END