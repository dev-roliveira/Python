""" Teste de Velocidade com Expressões Geradoras """

#  Generators (Geradores)


# def nums():

#    for num in range(1,10):
#        yield num


# ge1 = nums()

# print(ge1)  # Generator

#  Generator Expression
# ge3 = (num for num in range(1,10))


# Realizando o teste de Velocidade
import time

# Generator Expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))  # 100 milhões
gen_tempo = time.time() - gen_inicio

# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator levou {gen_tempo}')
print(f'List levou {list_tempo}')

