"""
Funções com Parâmetros ( de entrada )
Diferença entre Parâmetros e Argumentos

- Parâmetros são variáveis declaradas na definição de uma função
- Argumentos são dados passados durante a execução de uma função

Argumentos nomeados (Key Arguments)
- Caso utilizemos o nome dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem
Ex.

def nome_completo(nome, sobrenome):
    return f'Seu nome Completo é {nome} {sobrenome}'


nome = input('Digite seu Nome: ')
sobrenome = input('Digite seu Sobrenome: ')

print(nome_completo(nome, sobrenome))
print(nome_completo(sobrenome, nome))

- Funções que recebem dados para serem processados dentro da mesma;
- Com a entrada de dados diferentes, dependendo do processamento, a saída será diferente;

Há funções que:
- Não possuem entrada
- Não possuem saída
- Possuem entrada, mas não possuem saída
- Não possuem entrada, mas possuem saída
- Possuem entrada e saída

Funções podem ter vários parâmetros de entrada, desde que separados por vírgula.

Ex.
def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(multiplica(4, 5))
print(outra(3, 2, 'Geek '))



"""
# Refatorando uma função
# Antes


# def quadrado_de_7():
#    return 7 * 7

# Depois


# def quadrado(numero):
#    return numero * numero # Ou numero ** 2


# print(quadrado(7))
# print(quadrado(5))

def soma_impares(numero):
    total = 0
    for valor in numero:
        if valor % 2 != 0:
            total = total + valor
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
# print(soma_impares(lista))
