# -*- encoding: utf-8 -*-

"""
Quando fala-se em paradigmas de Programação:
Paradigmas de Programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

- Programação Estruturada
- Programação Orientada a Objetos
- Programação Funcional

A utilização desses paradigmas dependerá mais da linguagem utilizada para o trabalho.

O objetivo de utilizar POO é mapear objetos do mundo real para modelos computacionais, fazendo com que possamos
representar tais objetos com suas características e comportamentos.

Classe = Molde

Atributos = Características do Objeto, e uma classe pode ter nenhum ou vários atributos

Métodos = Comportamento do Objeto, entende-se métodos como sendo funções. A única diferença é que o métódo está dentro de
uma classe.

Construtor = Também é um método, mas é um método especial, é um método utilizado para criar os objetos a partir da nossa
classe

Objeto/Instância = Elementos que criamos baseado em nossa Classe

"""


class Produto:
    pass

ps4 = Produto() # utilizando o construtor
print(type(ps4)) # <class '__main__.Produto'>
print(ps4) # <__main__.Produto object at 0x0000027CF9D67970>

