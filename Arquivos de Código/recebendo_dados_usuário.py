"""
Recebendo dados do usuário...
input() -> Todo dado recebido via input é do tipo String (tudo que estiver entre aspas)
Cast -> Nomenclatura usada na conversão de um dado em outro tipo de dado
"""
# Exemplo antigo
# print("Qual seu nome?")
# nome = input()
# Exemplo novo
nome = input('Qual seu Nome? \n ')
# Exemplo antigo
# print("Seja Bem-Vindo(a) %s" % nome)
# Exemplo novo
# print('Seja Bem Vindo(a) {0}'.format(nome))
# Mais atual disponível a partir do 3.6
print(f'Seja bem vindo(a) {nome}')
# Exemplo antigo
# print("Qual sua idade?")
# idade = input()
# Exemplo novo
idade = input('Qual sua idade? \n')
# Exemplo antigo
# print("%s tem %s anos" % (nome, idade))
# Exemplo novo
# print('{0} tem {1} anos'.format(nome, idade))
# Mais atual disponível a partir do 3.6
print(f'{nome} tem {idade} anos')
print(f'E nasceu no ano de {2019 - int(idade)}')
