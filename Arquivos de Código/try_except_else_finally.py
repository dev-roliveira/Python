"""
Try, Except, Else, Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA, PRINCIPALMENTE ENTRADAS DE USUÁRIOS!

"""

'Uso do else'
# try:
#    num = int(input('Informe um numero: '))
# except ValueError:
#    print(f'Valor Incorreto')
# else:
#     print(f'Você digitou {num}')

'Uso do finally'
'geralmente utilizado para fechar ou desalocar recursos. (Fechar conexão com BD, Fechar arquivos abertos, etc...'
# try:
#    num = int(input('Informe um número: '))
# except ValueError:
#    print('Valor Incorreto')
# else:
#    print(f'Numero digitado: {num}')
# finally:  # se der erro, executa o erro e finally. se não der erro, executa else e o finally.
#    print('Depois do Bloco Try/Except')


def dividir(a, b):
    try:
        return int(a)/int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'O valor de 2 não pode ser zero'


num1 = input('Digite o Primeiro Numero: ')
num2 = input('Digite o Segundo Numero: ')

print(dividir(num1, num2))
