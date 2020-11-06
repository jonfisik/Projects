'''
Entrada de dados 05/11/2020
'''
a = '5.5'
b = int(float(a))
print (b)
nome = input('Digite seu nome: ')
print(f'O usuário digitou {nome} e o tipo da variável é '
      f'{type(nome)}')

print('-'*30)
nome2 = input('Qual seu nome? ')
idade2 = input('Qual sua idade? ')
ano_nasc = 2020 - int(idade2)
print(f'{nome} tem {idade2} anos. Seu ano de nascimento é {ano_nasc}.')
print('-'*30)

num1 = int(input('Digite 1° número: '))
num2 = int(input('Digite 2° número: '))
print(f'''
      - Soma {num1+num2} 
      - Subtração {num1-num2} 
      - Multiplicação {num1*num2} 
      - Divisão {num1/num2}''')