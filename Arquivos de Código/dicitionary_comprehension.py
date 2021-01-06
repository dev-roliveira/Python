"""
Dictionary Comprehension
Muda apenas a sintaxe se comparar à list comprehension


Analisando:
Para criar uma lista:
lista = [1, 2, 3, 4]

Para criar uma tuṕla:
tupla = (1, 2, 3, 4)

Para criar um set:
set = {1, 2, 3, 4}

Para criar um dicionário:
dict = {'a':1, 'b':2, 'c':3, 'd':4}



Sintaxe:
{chave:valor for valor in iteravel}

"""

'Exemplo 1'

# numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
# print(quadrado)

'Exemplo 2'

# numero = [1, 2, 3, 4, 5]
# quadrados = {valor: valor ** 2 for valor in numero}
# print(quadrados)

'Exemplo 3'

# chaves = 'abcde'
# valores = [1, 2, 3, 4, 5]
# mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
# print(mistura)

'Exemplo 4'
'Exemplo com lógica condicional'

# numeros = [1, 2, 3, 4, 5]
# res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
# print(res)
