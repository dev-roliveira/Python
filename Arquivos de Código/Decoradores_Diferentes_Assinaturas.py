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
# print(saudacao(nome))


# Refatorando com Decorator Pattern
# def gritar(funcao):
#    def aumentar(*args, **kwargs):
#        return funcao(*args, **kwargs).upper()
#    return aumentar



# @gritar
# def ordenar(principal, acompanhamento):
#    return f'Olá eu gostaria de {principal} com {acompanhamento}, por favor!'


# print(ordenar('Picanha', 'Arroz'))


# Decorator com Argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args,**kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto, primeiro argumento precisa ser {valor}'
            return funcao(*args,**kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)
