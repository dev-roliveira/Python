"""
Filter
A diferença entre map e filter é:

- map recebe dois parâmetros e retorna um objeto mapeando a função para cada elemento do iteravel.
- filter recebe dois parâmetros e retorna um objeto filtrando apenas os elementos de acordo com a função.


filter(função, iteravel) - > serve para filtrar dados de uma determinada coleção

Assim como a função map, a função filter recebe dois parâmetros. Sendo uma função e um iterável;
Assim como a função map, a função filter mantém o dado armazenado somente até a primeira utilização. (sempre retorna
true ou false)

O dado retornado da função é filter object

"""

'Filtro de Dados acima da média'
# import statistics

# dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# res = filter(lambda valor: valor > statistics.mean(dados), dados)
# print(list(res))

'Remoção de dados Faltantes'
# paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']
# print(list(filter(None, paises)))

'Filter Com Lambda'
# print(list(filter(lambda pais: len(pais) > 0, paises)))

# usuarios = [{'username': 'samuel', "tweets": ['Adoro Bolo', 'Adoro Pizza']},
#            {'username': 'carla', "tweets": ['Adoro meu gato']},
#            {'username': 'jeff', "tweets": []},
#            {'username': 'bob123', "tweets": []},
#            {'username': 'doggo', "tweets": ['Adoro cachorro', 'Vou sair hoje']},
#            {'username': 'gal', "tweets": []}]

# Filtrar os usuários que estão inativos no tweeter - Forma 1
# print(list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios)))

# Filtrar os usuários que estão inativos no tweeter - Forma 2
# print(list(filter(lambda usuario: not usuario['tweets'] == 0, usuarios)))

'Combinando filter e map'
nomes = ['Vanessa', 'Ana', 'Maria']

# Criar uma lista contendo 'sua instrutora é: ' + nome da instrutora, desde que cada nome tenha menos que 5 caracteres
print(list(map(lambda nome: f'Sua instrutura é {nome}', filter(lambda nome: len(nome) < 5, nomes))))
