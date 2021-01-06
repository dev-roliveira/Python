"""
Modos de Abertura de Arquivos

r - read
w - write (sobrescreve o arquivo existente)
x - abre para escrita, somente se o arquivo não existir
a - abre para escrita, adicionando o conteúdo ao final do arquivo não sendo possível alterar com seek()
+ - abre para atualização, sempre com outro comando, ele substitui o conteúdo


"""

with open('Castemere.txt', 'r+') as arquivo:
    print(arquivo.readlines())
