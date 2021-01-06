"""
Listas no Python
"""

type([])
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista
# num = 18
# if num in lista4:
#    print(f'Encontrei o número {num}')
# else:
#    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
# lista1.sort()
# print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
# print(lista1.count(1))

# Podemos facilmente adicionar elementos em listas
"""
Para adicionar elementos ou valores em listas, utilizamos a função append()
Com append nós só conseguimos adicionar um valor por vez
"""
# print(lista1)
# lista1.append([42, 23, 21])
# print(lista1)

"""
Para adicionar elementos separados utilizamos a função .extend([])
"""
# print(lista1)
# lista1.extend([42, 23, 21])
# lista1.sort()
# print(lista1)

# Podemos adicionar um novo elemento indicando a posição do índice, sem substituir o valor inicial
# lista1.insert(2, 'Novo Valor')
# print(lista1)

# Podemos facilmente juntar duas listas
# lista6 = lista1 + lista2
# print(lista6)

# Para imprimir a lista invertida usa-se .reverse()
# lista2.reverse()
# print(lista2)

# Para copiar uma lista utiliza-se .copy()
# lista6 = lista2.copy()
# print(lista6)

# Para verificar o tamanho de uma lista, usa-se o len()
# print(len(lista2))

# Para remover o último elemento da lista usa-se o .pop()
# Para remover um elemento pelo índice usa-se .pop(indice do elemento)
# lista5.pop()
# print(lista5)

# Para apagar todos os elementos usa-se o .clear()
# print(lista5)
# lista5.clear()
# print(lista5)

# Para converter str em uma lista, por padrão o split() separa os elementos pelo espaço em branco
# Para alterar o padrão, coloca o separador dentro do parênteses Ex. split(',')
# curso = 'Programação em Python Essencial'
# curso = curso.split()
# print(curso)

# Para converter uma lista em uma str, usa-se .jojn()
# lista6 = ['Programação', 'em', 'Python', 'Essencial']
# print(lista6)
# curso = ' '.join(lista6)
# print(curso)

# Para iterar sobre uma lista
# for elemento in lista1:
#    print(elemento, end="")

# Para acessar elementos de forma indexada usa-se nome_da_lista([posição do elemento])
# print(lista1)
# print(lista1[3])

# Para encontrar o indice de um elemento na lista usa-se.index
# print(lista1.index[2])

# Para retornar o indice do primeiro elemento encontrado usa-se .index(numero_procurado, indice_inicial_de_procura)
# print(lista.index(5, ))

# Buscar em um Range .index(valor_procurado, indice_inicio, indice_final)
# print(lista1.index(8, 3, 6)

# Usar slice
# lista[inicio:fim:passo]
# print(lista1[1:]) # Inicia do indice 1 e vai até o fim da lista

# Mostrar Soma, Valor Máximo, Valor Mínimo e Tamanho da Lista
# print(sum(lista1))
# print(max(lista1))
# print(min(lista1))
# print(len(lista1))

# Transformar lista em Tupla
# print(lista1)
# print(type(lista1))
# tupla = tuple(lista)
# print(tupla)
# print(type(tupla))

# Desempacotamento de listas
# lista = [1, 2, 3]
# num1, num2, num3
# print(num1)
# print(num2)
# print(num3)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy
# lista = [1, 2, 3]
# print(lista)
# nova = lista.copy()
# print(nova)
# nova.append(4)
# print(nova)

# Forma 2 - Shallow Copy
# lista = [1, 2, 3]
# print(lista)
# nova = lista
# print(nova)
# nova.append(4)
# print(nova)
# print(lista)
