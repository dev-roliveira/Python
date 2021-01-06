"""
**kwargs

É um parametro de entrada, como o args, porém que armazena os valores em um dicionário.

Nas funções, podemos ter (NESTA ORDEM)

- Parâmetros obrigatórios;
- args
- Parâmetros default
- kwargs


# Ex 1.


def cores(**kwargs):
    print(kwargs)


cores(marcos='verde')

# Ex 2.


def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores(marcos='verde')

# Desempacotando dados no kwargs
Obs. O nome das chaves devem ser os mesmo dos parâmetros da função;

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome':'Jones'}
print(mostra_nomes(**nomes))

"""

