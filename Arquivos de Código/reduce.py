"""
Reduce

Aplica a função dada nos dois primeiros elementos de uma coleção, guarda o valor e aplica a função no valor guardado e no
próximo elemento da coleção. Até finalizar a coleção.

OBS. A partir do Python 3, a função reduce não é mais uma função integrada (bult-in). Portanto deve-se importar antes,
através do módulo 'functools'.


dados = [a1, a2, a3, ... an]
def funcao(x,y):
    return x * y

A função reduce(), funciona da seguinte forma:
 - Passo 1: resultado1 = f(a1, a2)
   Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.

 - Passo 2: resultado2 = f(resultado1, a3)
   Aplica a função no resultado anterior e no próximo elemento da coleção e guarda o resultado.

 - Isso é repetido até o final da coleção.

 - No final reduce() retornará o valor final

"""

from functools import reduce
dados = [1, 2, 3]

# Para utilizar o reduce(), precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

'Utilizando um loop normal'
# res = 1
# for n in dados:
#    res = res * n
# print(res)
