"""
List Comprehension

- Gera novas listas com dados processados a partir de outro iteravel.

# Síntaxe

[ dado for dado in iteravel ]

"""

# Exemplo 1

# numeros = [1, 2, 3, 4, 5]
# res = [numero * 10 for numero in numeros]
# print(res)

"""
Para entender melhor, dividimos a função em 2 partes:

1 parte - for numero in numeros
2 parte - numero * 10

"""

# Exemplo 2
# res = [numero / 2 for numero in numeros]
# print(res)

# Exemplor 3
# def funcao(valor):
#    return valor * valor
# res = [funcao(numero) for numero in numeros]
# print(res)


'List Comprehension vs. loop'

# Com loop

# numeros = [1, 2, 3, 4, 5,]
# numeros_dobrados = []
# for numero in numeros:
#    numero_dobrado = numero * 2
#    numeros_dobrados.append(numero_dobrado)
# print(numeros_dobrados)

# Com List Comprehension
# print([numero * 2 for numero in [1, 2, 3, 4, 5]])

' Outros exemplos'

# Exemplo 4
# nome = 'Renan Oliveira'
# print([letra.upper() for letra in nome])

# Exemplo 5
# def caixa_alta(nome):
#    nome = nome.replace(nome[0], nome[0].upper())
#    return nome
# amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
# print([caixa_alta(amigo) for amigo in amigos])

# Exemplo 6
# print([numero * 3 for numero in range(1, 10)])

# Exemplo 7
# print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Exemplo 8
# print([str(numero) for numero in [1, 2, 3, 4, 5]])
