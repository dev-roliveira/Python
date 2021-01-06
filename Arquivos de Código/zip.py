"""
Zip

zip() - Cria um iteravel chamado zip_object que agrega elementos de cada um dos iteraveis passados como entrada em pares
      - O objeto some da memoria após a primeira utilização
      - Utiliza como parâmetro o menor tamanho em iteravel, isso significa que se estiver trabalhando com iteraveis de
        tamanhos diferentes, irá parar quando os elementos do menor iteravel acabar.

"""

'Exemplo 1'
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]

# zip1 = zip(lista1, lista2)
# print(zip1)
# print(list(zip1))  # [(1, 4, 1), (2, 5, 2), (3, 6, 3)]
# print(type(zip1))

'zip para dicionario'
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]

# zip1 = zip(lista1, lista2)
# print(dict(zip1))  # {1: 4, 2: 5, 3: 6}

'zip com diferentes iteraveis'
# tupla = (1, 2, 3, 4, 5)
# lista = [6, 7, 8, 9, 10]
# dicio = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
# zt = zip(tupla, lista, dicio.values())
# print(list(zt))

# dados = [(0,1), (1,2), (2,3), (3,4), (4,5)]
# print(list(zip(*dados)))  # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]


prova1 = [70, 40, 78]
prova2 = [98, 30, 98]
alunos = ['Sansa', 'Arya', 'Myrcella']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# usando map()
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
