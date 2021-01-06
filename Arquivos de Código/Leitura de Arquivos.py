"""
Leitura de Arquivos

Como ler o conteúdo de um arquivo usando Python.

Para ler um conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente signigica abrir.

open() -> Na forma mais simples de utilização, nós passamos apenas um parâmetro de entrada. Que neste caso é o caminho
do arquivo para ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

por padrão, a função open() abre o arquivo para LEITURA. Este arquivo deve existir, ou então teremos o
erro file not found error.




"""
# Exemplo

arquivo = open('Castemere.txt')

# print(arquivo)
"<_io.TextIOWrapper name='Castemere.txt' mode='r' encoding='UTF-8'>"

# print(type(arquivo))
"<class '_io.TextIOWrapper'>"

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
print(arquivo.read())

# Obs. O Python utiliza um recurso para trabalhar com arquivos chamado 'cursor'. Esse 'cursor' funciona como o cursor
# quando estamos escrevendo.

