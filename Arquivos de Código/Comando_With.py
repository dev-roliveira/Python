"""
Bloco with -> É utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with

"""

# O Bloco With
with open('Castemere.txt') as arquivo:
    print(arquivo.readlines())
