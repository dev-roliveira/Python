"""
Funções com Retorno

Aumentam a flexibilidade de utilização do dado que a função está gerando.

Em Python, quando uma função não retorna nenhum valor, o retorno é None.

Funções Python que retornam valores, devem retornar estes valores com a palavra reservada 'return'.
Obs1. Return finaliza a função, ou seja ela sai da execução da função.
Obs2. Podemos ter em uma função diferentes returns.
Obs3. Podemos em uma função retornar qualquer tipo de dado e até mesmo multiplos valores.

Não precisamos necessariamente criar uma variável para receber o retorno de uma função, podemos passar a execução da
função para outras funções.

Ex.

'Com variável'

def quadrado_de_sete():
    print(7*7)  # sem retorno
    return 7 * 7  # com retorno


ret = quadrado_de_sete()
print(ret)


'Sem Variável'
def quadrado_de_sete():
    return 7 * 7


print (quadrado_de_sete())


"""
# Exemplo 1 - Com return saindo da função
# def diz_oi():
#    return 'Oi'
# linhas abaixo dele, jamais será executado.


# print(diz_oi())

# Exemplo 2 - Com diferentes returns
# def nova_funcao():
#    variavel = None
#    if variavel:
#        return 4
#    elif variavel is None:
#        return 3.2
#    return 'b'

# print(nova_funcao())

# Exemplo 3 - Qualquer tipo de dados e multiplos valores
# def outra_funcao():
#    return 2, 3, 4, 5
# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)

# Exemplo 4 - Cara/Coroa

# from random import random


# def joga_moeda():
#    if random () > 0.5:
#        return 'Cara'
#    return 'Coroa'


# print(joga_moeda())


