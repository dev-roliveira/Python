"""
Map

Com Map fazermos mapeamento de valores para função.
Map é uma função que recebe dois parâmetros:
 - O primeiro é uma função
 - O segundo um iteravel
Map retorna um Map Object

Geralmente usa-se uma expressão lambda como função para o Map

Após utilizar a função map() depois da primeira utilização do resultado, ele zera.

"""

# import math


# def area(raio):
#    """ Calcula a área de um círculo com raio r """
#    return math.pi * (raio ** 2)
# print(area(2))
# print(area(5.3))


' Caso tenha uma lista devalores '
# raios = [2, 5, 7.1, 0.3, 10, 44]

' Forma Comum '
# areas = []
# for r in raios:
#    areas.append(area(r))
# print(areas)

' Forma Utilizando Map '
# areas = map(area, raios)
# print(list(areas))

' Forma de Map com Expressão Lambda '
# print(list(map(lambda r: math.pi * (r ** 2), raios)))

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('NY', 28),
           ('Londres', 22)]

# Converter as temperaturas para Farenheit
c_para_f = lambda dado: (dado[0], 9/5 * dado[1] + 32)
print(list(map(c_para_f, cidades)))
