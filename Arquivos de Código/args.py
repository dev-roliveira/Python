"""
Entendendo *args

- O *args é um parâmetro, como qualquer outro. Isso significa que você poderá chamar de qualquer coisa, desde que comece
com o asterisco. Ele coloca valores extras informados em uma entrada, numa tupla.

Exemplo
*xis

Mas por convenção, utilizamos *args para defini-lo




Exemplo de utilização:

def soma_todos_numeros(num, num2, num3):
    return num+num2+num3


print(soma_todos_numeros(4, 6, 9))

Neste exemplo, se for declarado um valor a menos ou a mais na entrada, dará erro.


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))

Com *args o erro é inexistente


Exemplo com lista:

def soma_todos(*args):
    return sum(args)


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_todos(lista))


Se for informada uma lista como args, dará erro.
Para resolver, devemos utilizar o desempacotador.

def soma_todos(*args):
    return sum(args)


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_todos(*lista)

# Utilização do Asterisco para desempacotar, informando ao Python que estamos passando como argumento,
uma coleção de dados. Desta forma ele saberá que precisará antes, desempacotar esses dados.



"""
