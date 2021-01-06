"""
Módulo Collections - Ordered Dict
Em um dicionário comum a ordem de inserção dos elementos não é garantida.
No Ordened Dict essa ordem de inserção é garantida.

"""
from _collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'Chave = {chave} : Valor = {valor}')
