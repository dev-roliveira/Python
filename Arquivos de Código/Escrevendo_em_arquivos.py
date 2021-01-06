"""
Escrevendo em Arquivos

OBS: Ao abrir um arquivo para leitura, não pode-se realizar a escrita. E vice-versa.
OBS: Ao abrir um arquivo para escrita, o arquivo é Criado no Sistema Operacional
"""

with open('Castemere.txt', 'w') as arquivo:
    arquivo.write('Chuvas de Castemere \n\n')
