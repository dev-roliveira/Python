"""
Decorators
- São funções
- Envolvem outras funções e aprimoram seus comportamentos
- São exemplos de HOF
- Tem uma sintaxe própria, usando @ (Syntact Sugar)

"""

# Decorator como função
# Sintaxe não recomendada


# def seja_educado(funcao):
#    def sendo():
#        print('Foi um Prazer')
#        funcao()
#        print('Tenha um Otimo Dia')
#    return sendo


# def saudacao():
#    print('Seja Bem Vindo(a)')


# Testando 1
# teste = seja_educado(saudacao)
# teste()


# Sintaxe Recomendada
def sendo_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo


@sendo_educado_mesmo
def apresentando():
    print('Meu nome é Arya')


apresentando()

