"""
Min e Max

max() -> Retorna o maior valor em um iteravel, ou o maior de dois ou mais elementos
min() -> Retorna o menor valor em um iteravel, ou o menor de dois ou mais elementos
"""

# lista = [1, 8, 4, 99, 34, 129]
# tupla = (1, 8, 4, 99, 34, 129)
# conjunto = {1, 8, 4, 99, 34, 129}
# dicionário = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
# print(max(lista))
# print(max(tupla))
# print(max(conjunto))
# print(max(dicionário.values()))

'Verificando entre dois valores'
# val1 = int(input('Numero 1: '))
# val2 = int(input('Numero 2: '))
# print(max(val1, val2))

'Verificando entre strings'
# nomes = ['Arya', 'Jon', 'Bran', 'Sansa']
# print(max(nomes))  # Arya, pois incia-se com 'A'
# print(min(nomes))  # Sansa, pos inicia-se com 'S"
# print(max(nomes, key=lambda nome: len(nome)))  # Sansa
# print(min(nomes, key=lambda nome: len(nome)))  # Jon

'Verificando em Dicionario'

# musicas = [{"titulo": "Thunderstuck", "Tocou": 3},
#           {"titulo": "Dead Skin Mask", "Tocou": 2},
#           {"titulo": "Back in Black", "Tocou": 4},
#           {"titulo": "Iron Man", "Tocou": 32}]

# print(max(musicas, key= lambda musica: musica['Tocou']))
# print(min(musicas, key= lambda musica: musica['Tocou']))
# print(max(musicas, key= lambda musica: musica['Tocou'])['titulo'])  # Somente o titulo
# print(min(musicas, key= lambda musica: musica['Tocou'])['titulo'])  # Somente o titulo

