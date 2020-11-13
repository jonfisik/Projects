'''
Operador ternário em python
'''

logged_user = True
idade = 17
# if logged_user: #logged_user == True
#     msg = 'Usuário logado.'
# else:
#     msg = 'Usuário precisa logar.'

msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
print(msg)
maior_idade = (idade >= 18)
msg2 = 'Pode acessar' if maior_idade else 'Não pode acessar.'
print(msg2)
print('-'*30)

idade = input('Qual sua idade? ')
if not idade.isnumeric():
    print('Digite apenas número.')
else:
    idade = int(idade)
    maior_idade = (idade >= 18)
    msg3 = 'Pode acessar' if maior_idade else 'Não pode acessar.'

print(msg3)