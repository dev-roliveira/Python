"""
Decorators com Diferentes Assinaturas

Ou seja com Diferentes Parâmetros de Entradas
- Usando Decorator Pattern

"""


# Relembrando Decorator
# def gritar(funcao):
#    def aumentar(nome):
#        return funcao(nome).upper()
#    return aumentar

# @gritar
# def saudacao(nome):
#    return f'Olá eu sou {nome}'
# print(saudacao('Rob Stark'))


# Decorator Pattern
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá eu gostaria de {principal} com {acompanhamento}, por favor!'


print(ordenar('Picanha', 'Arroz'))
