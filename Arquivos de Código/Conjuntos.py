"""
Conjuntos

- Conjuntos (em qualquer linguagem de programação) são referências à Teoria dos Conjuntos da Matemática

- No Python, os conjuntos são chamados de "Sets". Dito isso, da mesma forma que na matemática, sets (conjuntos), não
possuem valores duplicados.

- Sets (conjuntos), não possuem valores ordenados.
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados.

- Conjuntos são utilizados para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles.
- Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os Conjuntos são referenciados em Python com chaves {}

Diferença entre conjuntos (Set) e Mapas (Dicionários):

- Um dicionário tem chave/valor
- Um set tem apenas valor

"""
# Definindo um conjunto
# Forma 1
# s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Há valores repetidos, e serão ignorados.
# print(s)

# Forma 2 - Mais Comum
s = {1, 2, 3, 4, 5, 5}
# print(s)

# Podemos verificar se determinado elemento está contido no conjunto
# if 3 in s:
#    print('ok')
# else:
#    print('não tem')

# Importante lembrar que além de não termos valores duplicados, não temos ordem

s = {99, 2, 34, 23, 12, 1, 44, 5, 2, 34}
lista = [99, 2, 34, 23, 12, 1, 44, 5, 2, 34]
tupla = 99, 2, 34, 23, 12, 1, 44, 5, 2, 34
dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 2, 34], 'dict')

# print(s)
# print(lista)
# print(tupla)
# print(dicionario)

# Assim como todos outros conjuntos, podemos colocar tipos de dados misturados em Sets

# Podemos iterar normalmente em um set
# for valor in s:
#    print(valor)

# Usos interessantes com Sets
# Formulário de Cadastro de visitantes

# cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

# Saber quantas cidades distintas
# print(len(set(cidades)))

# Adicionando elementos em um conjunto
# s = {1, 2, 3}
# s.add(4)
# print(s)

# Remover valor em um conjunto
# Forma 1
# s.remove(3)  # informamos o valor a ser removido
# print(s)

# Forma 2
# s.discard(2)
# print(s)

# Copiando um Conjunto para outro
# Forma 1 - Deep Copy
# novo = s.copy()
# print(novo)

# Forma 2 - Shallow Copy
# novo = s
# print(novo)

# Remover todos os itens de um conjunto
# s.clear()

# Métodos Matemáticos de Conjuntos
# Imagine que temos dois conjuntos, um do curso python e um de java

estudantes_python = {'Marcos', 'Patricia', 'Helen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
# print(unicos1)

# Forma 2 - Utilizando o caractere pipe "|"
unicos2 = estudantes_java | estudantes_python
# print(unicos2)

# Gerar um conjunto de estudantes que estão nos dois cursos

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
# print(ambos1)

# Forma 2 - Utlizando &
ambos2 = estudantes_java & estudantes_python
# print(ambos2)

# Gerar um Conjunto de Estudantes de um curso que não estão em outro com difference
so_python = estudantes_python.difference(estudantes_java)
# print(so_python)

so_java = estudantes_java.difference(estudantes_python)
# print(so_java)

# Soma, Valor Maximo, Valor Minimo e Tamanho

c = {1, 2, 3, 4, 5, 6}
print(sum(c))
print(max(c))
print(min(c))
print(len(c))
