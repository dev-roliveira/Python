"""
Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo OS.

"""

import os

# getcwd() -> Pega o Current Work Directory
os.getcwd()

# chdir() ->Para mudar o diretorio
# os.chdir('..')

# path.isAbs -> Verificar se diretório é relativo ou absoluto
# print(os.path.isabs())

# os.name -> Verificar o nome do Sistema
# print(os.name)

# Criar Diretórios
# res = os.path.join(os.getcwd(), 'Geek')
# os.chdir(res)
# print(os.getcwd())

# Listar os Diretorios
# print(os.listdir())

# Listar os Diretorios com mais detalhes
scanner = os.scandir()
arquivos = list(scanner)


print(arquivos[0].inode()) # Número do Arquivo
print(arquivos[0].is_dir()) # É Diretório?
print(arquivos[0].is_file()) # É Arquivo?
print(arquivos[0].is_symlink()) # É um link simbolico?
print(arquivos[0].name) # Nome do Arquivo
print(arquivos[0].path) # Caminho do Arquivo
print(arquivos[0].stat()) # Estatísticas

scanner.close()
