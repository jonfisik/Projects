'''
Exercício - list comprehenson
'''
# exemplo
carrinho = []
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 50.5))
carrinho.append(('Produto 3', 120))
carrinho.append(('Produto 4', 10))

# total = 0
# for item in carrinho:
#     total.append(float(item[1]))
# print(f'>>> {total}. Total R$ {sum(total)}')

#total = [(x, y) for x, y in carrinho]
total = sum([float(y) for x, y in carrinho])
valores_produto = [float(y) for x, y in carrinho]
print(f'>>> {valores_produto}. Total R$ {total}')

