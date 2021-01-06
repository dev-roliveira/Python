"""
Seek e Cursor

seek() -> É utilizada para movimentar o cursor pelo arquivo
          Ela recebe um parâmetro de onde queremos colocar o cursor.


"""

arquivo = open('Castemere.txt')
print(arquivo.read())

# Movimentando o Cursor pelo Arquivo
arquivo.seek(0)  # seek(0) retorna o cursor para o inicio

# readline() -> Função que lê o arquivo linha a linha
print(arquivo.readline())

# readlines() -> Função que lê o arquivo linha a linha e armazena em uma lista
# print(arquivo.readlines())

# close() -> Fechar o steraming com o arquivo
arquivo.close()
