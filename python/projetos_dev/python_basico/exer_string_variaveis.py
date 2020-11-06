'''
* Criar variáveis para nome(str), idade (int), altura (float) e peso (float) de uma pessoa
* Criar variável para ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade da pessoa e no ano atual)
* Obter o IMC da pessoa com duas casas decimais (peso e altura)
* Exibir um texto com todos os valores na tela usando f-string (com chaves)
'''

nome = 'Zé'
idade = 50
altura = 1.65
peso = 75.5
ano_atual = 2020
ano_nascimento = ano_atual - idade
imc = peso / (altura*altura)

print(f'{nome}, nascido no ano de {ano_nascimento}, tem {idade} anos e {peso} kg. Seu IMC é {imc:.2f}.')

print('"Já sei"')