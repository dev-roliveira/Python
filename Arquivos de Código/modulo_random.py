"""
Modulo Random e o que são modulos

- Em Python, módulos são outros arquivos Python.
- São uteis para reutilização de codigo e deixar a programação mais simples
- É possivel importar funções de outros modulos para utilização

Modulo Random possui várias funções para geração de números pseudo-aleatórios entre 0 e 1
Modulo Random é muito utilizado em RNA para pesos

"""

'Existem duas formas de utilizar um modulo ou função'
'Forma 1 - Importando todo o modulo e todos os atributos, funções, classes e propriedades que estiverem dentro do modulo'

# import random
# print(random.random())  # Para utilizar a função random do pacote random, colocamos pacote.função

'Forma 2 - Importando o modulo com a função desejada'

# from random import random

# for i in range(10):
#    print(random())

'Para utilizar numeros inteiros maiores que 1'
'usar a função uniform, que gera um numero pseudo-aleatorios entre os numeros pre-estabelecidos'

# from random import uniform
# for i in range(10):
#    print(uniform(3, 7))

'Para gerar valores pseudo-aleatorios inteiros'
'usa a função randoint()'

# from random import randint
# for i in range(6):
#    print(randint(1,61),end=',')

'Para mostrar um valor aleatorio entre um iteravel'
'usa a função choice'

# from random import choice
# jogadas = ['pedra', 'papel', 'tesoura']
# print(choice(jogadas))

'Para embaralhar dados'
'usa a função shuffle'

from random import shuffle
# cartas = ['K', 'A', 'Q', 'J', '10']
# shuffle(cartas)
# print(cartas)

