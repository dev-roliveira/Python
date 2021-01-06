"""
Dicionários (Dict)

Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor

[0, 1, 2] - Chave (índice)
[1, 2, 3] - Valor em lista
(1, 2, 3) - Valor em tuplas

Em dicionários as chaves não ficam implicitas como em listas e tuplas (que enxergamos somente quando usamos funções)
Dicionários são representados por {}.

Sintaxe:
variàvel = {'chave' : 'valor'}

Chaves e Valores podem ser de qualquer tipo.

Dicionários permitem Deep e Shallow Copy


"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Forma 1 - Mais comum de construção
# paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# print(paises)
# print(type(paises))

# Forma 2 - Menos comum de construção
# paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
# print(paises)
# print(type(paises))

# Acessando elementos
# Forma 1 - Acessando via chave, como em lista/tupla
# print(paises['br'])

# Forma 2 - Acessando via get
# Forma mais recomendada, caso busque um valor inexistente não da erro, da o tipo de dado 'none', um tipo vazio.
# print(paises.get('br'))

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
# pais = paises.get('ru', 'Russia')  # o código procurará 'ru' no dicionário e se não encontrar imprimirá 'Russia'
# print(pais)

# Verificar se o item está em uma Chave no Dicionario
print('br' in paises)

# Adicionar elementos em Dicionários
# receita = {'jan': 100, 'fev': 120, 'mar': 300}
# print(receita)

# Forma 1 - dicionario['chave'] = valor (Mais comum)
# receita['abr'] = 350
# print(receita)

# Forma 2 - variável = {chave : valor} e depois dicionario.update(variável)
# novo_dado = {'mai': 400}
# receita.update(novo_dado)
# print(receita)

# Atualizando dados em Dicionário
# Forma 1
# receita['mai'] = 550
# print(receita)

# Forma 2
# receita.update({'mai': 600})
# print(receita)

# Remover dados de um dicionário
# Forma 1 - usando .pop() sendo obrigatório indicar a chave. Ao removermos um objeto, o valor do objeto será retornado
# Forma mais comum
# ret = receita.pop('fev')
# print(ret)
# print(receita)

# Forma 2 - usando a função del
# print(receita)
# del receita['fev']
# print(receita)

# Forma não usual de criação de dicionário com .fromkeys(_chave: _valor)
# outro = {}.fromkeys('a', 'b')
# print(outro)
# print(type(outro))
