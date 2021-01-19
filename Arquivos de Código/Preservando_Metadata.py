"""
Preservando Metadatas com Wraps

- Metadatas: sao dados intrisecos em arquivos
- Wraps: sao funcoes que envolvem elementos com diversas finalidades

# Problema

def ver_log(funcao):
    def logar(*args, **kargs):
        ""Funcao dentro de Outra""
        print(f'Chamando funcao {funcao.__name__}')
        print(f'Chamando funcao {funcao.__doc__}')
        return funcao(*args,**kargs)
    return logar

@ver_log
def soma(a,b):
    ""Soma dois Numeros""
    return a + b

print(soma.__name__) # era pra ser soma, deu 'logar'
print(soma.__doc__) # era pra ser soma dois numeros, deu 'funcao dentro de outra'

"""

# Resolucao do Problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kargs):
        """Funcao dentro de Outra"""
        print(f'Chamando funcao {funcao.__name__}')
        print(f'Chamando funcao {funcao.__doc__}')
        return funcao(*args,**kargs)
    return logar

@ver_log
def soma(a,b):
    """Soma dois Numeros"""
    return a + b

print(soma.__name__) # soma
print(soma.__doc__) # soma dois numeros
