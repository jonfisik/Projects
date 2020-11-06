'''
Formatação de strings
'''
nome = 'Luiz Otávio'
idade = 32
altura = 1.80
peso = 80
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc,'.')
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}.')
print('{} tem {} anos de idade e seu IMC é {:.2f}.'.format(nome, idade, imc))
print('{1} tem {2:.2f} anos de idade e seu IMC é {0}.'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é {im:.2f}.'.format(n=nome, i=idade, im=imc))