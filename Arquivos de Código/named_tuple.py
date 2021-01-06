"""
Módulo Collections - Named Tuple

São tuplas diferenciadas, onde especificamos um nome para a mesma e também parâmetros.

"""
from collections import namedtuple
# Precisamos definir o nome e parâmetros

# Declaração da Tupla
# Forma 1
cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])


# Usando
ray = cachorro(idade=2, raça='Chow Chow', nome='Ray')
print(ray)

# Acessando dados na namedtuple
# Forma 1
print(ray[0])  # para acessarmos o valor referente à idade

# Forma 2
print(ray.idade)

