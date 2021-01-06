"""
Utilizando Lambdas

Conhecidas por expressões Lambdas, ou simplesmente Lambdas, são funções sem nome. Ou seja, funções anônimas.

Normalmente usada para filtragem e ordenação de dados

"""

'Função Python'
# def funcao(x):
#    return 3 * x + 1
# print(funcao(4))

'Expressão Lambda - Criação'
# lambda x: 3 * x + 1

'Expressão Lambda - Utilização'
# calc = lambda x: 3 * x + 1
# print(calc(4))

'Expressão Lambda, podem ter multiplas entradas'
# nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

'Expressão Lambda sem entrada'
# teste = lambda: 'Como?'
# print(teste())

'Expressão Lambda com lista - Uso mais correto da função'
# autores = ['J. K. Rowlinkg', 'Arthur Conan Doyle', 'R. R. Tolkien']
# print(autores)
# autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1])
# print(autores)

'Expressão Lamda para função quadrática'
'Função Quadrática: f(x) = a*x² + b*x + c'
# def geradora_função(a, b, c):
#    """Retorna a Função: f(x) = a*x² + b*x + c """
#    return lambda x: a * x ** 2 + b * x + c
# teste = geradora_função(2, 3, -5)
# print(teste(0))
# print(teste(1))
# print(teste(2))

