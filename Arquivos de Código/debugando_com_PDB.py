"""
Debugando com PDB (Python Debugger)


"""
'Debugando com Pycharm'
'Clica qual linha colocar um breakpoin, clicando no numero da linha'
'Clica em Debug'
# def dividir(a, b):
#    try:
#        return int(a)/int(b)
#    except ValueError:
#        return 'Valor Incorreto'
#    except ZeroDivisionError:
#        return 'O valor de 2 não pode ser zero'
# print(dividir(4, 6))

'Debugando com PDB'
'Para utilizar o PDB, precisa-se importar a biblioteca PDB*'
'E, então utilizar a função set_trace()'
'Coloca pdb.set_trace() logo acima da linha que deseja debugar'
"""Comandos Básicos do PDB:" 
"'l' para listar onde estamos no codigo" 
"'n' para proxima linha" 
"'p' imprime a variavel"
"'c' continua a execução (finaliza o debug"""

# import pdb

# nome = 'Sansa'
# sobrenome = 'Stark'
# pdb.set_trace()
# nome_completo = nome + ' ' + sobrenome
# curso = 'Matar Lannysters'
# final = nome_completo + ' faz o curso ' + curso
# print(final)

""" * A partir do Python 3.7 não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado 
como função built-in, chamada breakpoint(). """

'Exemplo com breakpoint()'

nome = 'Sansa'
sobrenome = 'Stark'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Matar Lannysters'
final = nome_completo + ' faz o curso ' + curso
print(final)
