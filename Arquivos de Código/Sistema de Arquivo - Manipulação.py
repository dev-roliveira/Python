"""
Sistema de Arquivo - Manipulação

"""
import os

# Descobrindo existência de Arquivo Relativo
# print(os.path.exists('Castemere.txt'))

# Descobrindo existência de Diretório Relativo
# print(os.path.exists('Castemere'))

# Descobrindo existência de Arquivo Absoluto
# print(os.path.exists('/home/renan/PycharmProjects/geekuniversityppe/Castemere.txt'))

# Descobrindo existência de Diretório Relativo
# print(os.path.exists('/home/renan/PycharmProjects/geekuniversityppe'))

# Criando arquivos
# Forma 1
# open('Teste.txt', 'w').close()
# Forma 2
# with open('Teste.txt', 'w') as arquivo:
#    pass
# Forma 3
# os.mknod('Teste.txt')

# Criando Diretórios Únicos
# os.mkdir('Nome ou Caminho para o Diretório')

# Criando múltiplos Diretórios
# os.makedirs('Nomes ou Caminhos dos Diretórios')
# Se os Diretórios existire, dará FileExistsError, e para corrigir:
# os.makedirs('Nomes ou Caminhos dos Diretórios', exist_ok=True)

# Renomear Arquivos e Diretórios
# os.rename('Diretório ou Arquivo', 'Novo Nome')

# Deletando Arquivos
# os.remove('Nome do Arquivo.txt')

# Deletando Diretórios Vazios
# os.rmdir('Nome do Diretório')

# Deletando uma Árvore de Diretórios
# for arquivo in os.scandir('Nome do Diretorio'):
#    if arquivo.is_file():
#        os.remove(arquivo.path)
#    if not arquivo.is_file():
#        os.rmdir(arquivo.path)

# Arquivos Temporários
# import tempfile

# with tempfile.TemporaryDirectory() as tmp:
#    print(f'Diretório Temporário Criado em {tmp}')
#    with open(os.path.join(tmp, 'arquivo temporário.txt'), 'w') as arquivo:
#        arquivo.write('Khal Drogo \n')
#    input()

# Criando Diretório Temporário, abrindo e criando um arquivo temporário
# input() é usado apenas para mantê-los 'vivos' dentro do bloco with

