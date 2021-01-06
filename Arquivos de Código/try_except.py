"""
Bloco Try / Except

É utilizado para tratar erros que podem ocorrer no código, prevenindo que o programa pare de funcionar e o usuário
receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    // execução problemática
except:
    //o que deve ser feito caso dê problemas
"""

'Exemplo 1 - Tratando um erro genérico'
# try:
#    geek()
# except:
#    print('Deu algum problema, tente novamente')

'Exemplo 2 - Tratando um erro específico (NameError)'
# try:
#    geek()
# except NameError:
#    print('Entrada Inválida, tente novamente')

'Exemplo 3 - Nomeando um erro específico'
# try:
#    geek()
# except NameError as err:
#    print(f'A aplicação gerou o seguinte erro: {err}')

'Exemplo 4 - Tratando diferentes tipos de erros'
# try:
#    geek()
# except NameError as erra:
#    print(f'Deu NameError: {erra}')
# except TypeError as errb:
#    print(f'Deu TypeError: {errb}')
# except:
#    print('Deu um erro diferente')

'Exemplo 5 - Tratando erro em função'


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {'nome':'geek'}
print(pega_valor(dic, 'game'))


