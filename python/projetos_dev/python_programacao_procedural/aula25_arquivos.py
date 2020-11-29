## Manipilando arquivos

## Criando, escrevendo e lendo arquivo
file = open('abc.txt', 'w+')
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')
## posicionado o cursor para a leitura do arquivo
file.seek(0, 0)
print('Lendo arquivo')
print(file.read(), end='')
print('-'*15)
# lendo linha por linha
file.seek(0 ,0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('-'*15)
## Lista
file.seek(0, 0)
print(file.readlines())
print('-'*15)
##
file.seek(0, 0)
for linha in file:
    print(linha, end='')

file.close()
print('-'*15)

## w: apaga tudo dentro do arquivo e escreve, r: ler
## a: adiciona-se ao arquivo sem apagar o conteúdo
with open('abcd.txt', 'w+') as file:
    file.write('Linha1 linha1 linha1 \n')
    file.write('Linha2 linha2 linha2 \n')
    file.write('Linha3 linha3 linha3 \n' *2)

    file.seek(0)
    print(file.read(), end='')
print('-'*15)

with open('abcd.txt', 'a+') as file:
    file.write('Outra linha \n')
    file.seek(0)
    print(file.read())

## Remove arquivo
# import os
# os.remove('abc.txt')