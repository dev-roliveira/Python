"""
Módulo Collections - Default Dict

São dicionários com todas as funções conhecidas, porém com as diferenças:

- ao criar um dicionário utilizando o Default Dict, nós informamos um valor default, podendo utilizar um lambda para isso
  esse valor será utilizado sempre que não houver um valor definido. Caso, tentemos acessar uma chave que não exista,
  essa chave será criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entradas e retornar valores.

"""

from _collections import defaultdict
dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'PEE'
print(dicionario)
print((dicionario['outro']))
print(dicionario)
