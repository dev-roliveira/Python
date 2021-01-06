"""
StringIO -> Utilizado para ler e criar arquivos em memória

Para ler ou escrever dados em arquivos do Sistema Operacional, o software precisa ter permissão

"""

from io import StringIO
mensagem = 'Apenas uma String Normal'

# Podemos criar um arquivo em memória, já com uma string inserida, ou vazia
arquivo = StringIO(mensagem)

