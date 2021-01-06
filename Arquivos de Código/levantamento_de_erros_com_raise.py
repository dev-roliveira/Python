"""
Raise -> lança exceções

raise não é uma função, é uma palavra reservada.
raise serve para criar as próprias exceções e mensagens de erro.

A forma geral de utilização é:
raise TipoDoErro('Mensagem de Erro')

raise assim como return finaliza a função.

"""

'Exemplo 1'
# raise ValueError('Valor Incorreto')

'Exemplo 2'


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto Precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('Cor Precisa ser uma String')
    if cor is not cores:
        raise ValueError('Cor não pré-definida')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Roberth', 'roxo')
# TypeError: Cor Precisa ser uma String
