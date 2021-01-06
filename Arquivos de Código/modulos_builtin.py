"""
Modulos Built-In

Modulos que já vem por padrão instalados no Python porém que precisam de importação

"""
'Utilizando alias (apelidos) para modulos'
# import random as apelido_do_modulo
# print(apelido_do_modulo.random())

'Importar todas as funções de um modulo com * '
'É diferente de import random, pois neste caso precisaria colocar no codigo random.função_desejada'
# from random import *
# print(random())

'Utilizando alias (apelidos) para funções'
# from random import função as apelido_da_função
# print(apelido_da_função)

'Importando vários imports de um mesmo módulo'
# from random import (
#                    random,
#                    randint,
#                    shuffle,
#                    choice
# )
