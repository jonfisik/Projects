__author__  = 'Jonatan Paschoal'
__version__ = '1.0.0'
__email__   = 'jonfisik@hotmail.com'
__status__  = 'Professor - Física'
__date__    = '22/12/2021'
'''
Data em python
'''

import datetime

#
# Data corrente
#
data = datetime.datetime.now()
nasc = datetime.datetime(1988,3,7)
print(' ')
print(f'Data/Hora: {data}')
print(' ')
print(f'{data.day}/{data.month}/{data.year}')
print(' ')
print(nasc)
print(nasc.strftime('%A'))
print(nasc.strftime('%a'))
print(nasc.strftime('%b'))
print(nasc.strftime('%W'))
print(nasc.strftime('%W'))
print(' ')
#
# %a dia da semana abreviado
# %A dia da semana completo
# %w número do dia da semana 
# %d número dia do mês
# %b texto mês abreviado
# %B texto mês
# %m número do mês 
# %y Ano com dois dígitos
# %Y Ano com quatro dígitos
# %H 00 - 23
# %I 00 - 12
# %p AM/PM
# %M minutos
# %s segundos 
# %f microsegundos
# %j dia do ano  001 - 365 
# %W número da semana
# # 
