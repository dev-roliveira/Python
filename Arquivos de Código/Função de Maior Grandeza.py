"""
Função de Maior Grandeza ou Higher Order Function

O que significa?
- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como
resultado ou mesmo que podemos passar funções como argumentos para outras funções e até mesmo criar variáveis do tipo
de funções nos nossos programas.

Obs. Na seção de funções nós utilizamos isso.

"""

# Exemplos
# Definindo as Funções


def somar(x,y):
    return x + y


def diminuir(x,y):
    return x - y


def multiplicar(x,y):
    return x * y


def divisão(x,y):
    return x/y


def calcular(num1, num2, funcao):
    return funcao(num1,num2)


#print(calcular(4, 3, somar))
#print(calcular(4, 3, diminuir))
#print(calcular(4, 3, multiplicar))
#print(calcular(4, 3, divisão))

# Nested Functions - Funções Aninhadas
# Funções dentro de Funções

