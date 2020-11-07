'''
Prévia documentação e função. 07-11-2020
try ~ if
    bloco comandos
except ~ else
    blocos comando

pass ~ ... segura o espaço para escrever o código posteriormente

valor =  False
if valor:
    pass # ou ... (pass, ellipsis)
else:
    print('texto')
'''


import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


###########
#  USAGE  #
###########

# float
print(is_float('-101.0112'))  # True
# int
print(is_int('-1010112'))  # True
# number in general (float or int)
print(is_number('-101.0112'))  # True

# False
print(is_number('123a'))  # False