"""
Listas Aninhadas (Arrays Multidimensionais ou Matrizes)

- Algumas linguagens de programação (C, Java, PHP) possuem uma estrutura de dados chamadas de arrays:
  - unidimensionais (Arrays/Vetores;
  - multidimensionais (Matrizes)

- Em Python temos somente listas, não existem arrays.

"""

# Exemplo 1
# listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # matriz 3x3
# print(listas)

'Como acessar os dados'
# print(listas[0])  # para acessar o primeiro elemento (linha)
# print(listas[0][2])  # para acessar o numero 3 (coluna)

'Iterar com loops em uma lista aninhada'
# for lista in listas:
#    for valor in lista:
#        print(valor)

'List Comprehension em lista aninhada'
# [[print(valor) for valor in lista] for lista in listas]

'Gerando um tabuleiro ou matriz 3 x 3'
# tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
# print(tabuleiro)

'Gerando jogadas para tic tac toe'
# velha = [['X' if not num % 2 else 'O' for num in range(1, 4)] for valor in range(1, 4)]
# print(velha)

'Gerando valores iniciais'
# print([['*' for i in range(1, 4)]for j in range(1, 4)])
