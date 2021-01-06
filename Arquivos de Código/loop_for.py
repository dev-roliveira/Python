""""
Estruturas de Repetição

Loop - Estrutura de repetição
for - uma das estruturas de repetição


"""

nome = "Renan"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que transformar ainda em uma lista

# Iterando sobre uma String
for letra in nome:
    print(letra)

# Iterando sobre uma Lista
for numero in lista:
    print(numero)

# Iterando sobre Range
for numero in numeros:
    print(numero)

# Iterando com enumerate
"""
enumerate:

((0, 'R'), (1, 'e'), (2, 'n'), (3, 'a'), (4, 'n'))

"""
for valor in nome:
    print(valor)
