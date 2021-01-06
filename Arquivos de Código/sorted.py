"""
Sorted

sorted() serve para ordenar elementos em qualquer iteravel.
Obs. Não confundir com sort(). O sort() funciona apenas em listas.

sorted() não modifica a lista, retorna uma lista com os elementos ordenados. O conjunto original mantém-se intacta.
sorted() sempre retorna uma LISTA com os elementos do iteravel ordenados
"""

# Exemplo 1
# numeros = {6, 8, 1, 2}
# print(numeros)

# print(sorted(numeros))  # Ordenar do menor para o maior

'Adicionando parâmetros ao sorted()'
# numeros = {6, 8, 1, 2}
# print(sorted(numeros, reverse=True))  # Ordena do maior para o menor

'sorted() para dicionarios'

# usuarios = [{'username': 'samuel', "tweets": ['Adoro Bolo', 'Adoro Pizza']},
#            {'username': 'carla', "tweets": ['Adoro meu gato']},
#            {'username': 'jeff', "tweets": []},
#            {'username': 'bob123', "tweets": []},
#            {'username': 'doggo', "tweets": ['Adoro cachorro', 'Vou sair hoje']},
#            {'username': 'gal', "tweets": []}]

# print(sorted(usuarios, key=lambda usuario: usuario['username']))  # Ordena pelo nome de usuario
# print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))  # Ordena pela quantidade de tweets


# musicas = [{"titulo": "Thunderstuck", "Tocou": 3},
#           {"titulo": "Dead Skin Mask", "Tocou": 2},
#           {"titulo": "Back in Black", "Tocou": 4},
#           {"titulo": "Iron Man", "Tocou": 32}]

# print(sorted(musicas, key=lambda musica: musica['Tocou']))  # Ordenar da Menos tocada para a mais tocada
# print(sorted(musicas, key=lambda musica: musica['Tocou'], reverse=True))  # Ordenar da Mais tocada para a menos tocada
# print(sorted(musicas, key=lambda musica: musica['titulo']))  # Ordenar pelo título