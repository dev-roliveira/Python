"""
Generators (Tuple Comprehension)

Generators ocupa menos espaço em memória se comparado à List, Dict ou Set Comprehension
Generators são mais performáticos
"""

# nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']


# List Comprehension
# res = [nome[0] == 'C' for nome in nomes]
# print(res)

# Generator
# res = (nome[0] == 'C' for nome in nomes)
# print(res)

'Comparando tamanho alocado'
# from sys import getsizeof
# list_comp = getsizeof([x * 10 for x in range(1000)])
# set_com = getsizeof({x * 10 for x in range(1000)})
# dict_com = getsizeof({x: x * 10 for x in range(1000)})
# generator = getsizeof(x * 10 for x in range(1000))
# print(list_comp)
# print(set_com)
# print(dict_com)
# print(generator)

'Iterando no Generator'
# gen = (x * 10 for x in range(1000))
# for numero in gen:
#    print(numero)
