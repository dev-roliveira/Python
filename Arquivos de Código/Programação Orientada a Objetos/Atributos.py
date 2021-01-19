# -*- encoding: utf-8 -*-

"""
Divide-se em três grupos:

- Atributos de Instância
- Atributos de Classe ou Estáticos
- Atributos Dinâmicos



- Atributos de Instância:
  São atributos declarados dentro do método construtor. (Método especial, utilizado para a construção do objeto).
  Significa que ao criarmos instâncias, de uma classe, todas as instâncias terão esses atributos.

Exemplo:

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

- Atributos Públicos e Privados:
  Trata-se da visibilidade deses atributos, quando declara-se um atributo como privado, ele só poderá ser usado dentro da
  própria classe que foi declarado.

  Em Python, por convenção ficou estabelecido que todo atributo de uma classe é público.

  Ou seja, pode ser acessado em todo o projeto.

  Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser acessdo/utilizado
  somente dentro da própria classe onde está declarado, utiliza-se Duplo Underscore no início de seu nome (conhecido
  também como name mangling).

Exemplo:

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo



- Atributos de Classe/Estáticos:
  São atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um
  valor e este valor é compartilhado entre todas as instâncias da classe, ou seja, ao invés e cada instância ter seus próprios
  valores como é o caso dos Atributos de Instância, com os Atributos de Classe todas as instâncias terão o mesmo valor para
  este atributo.

Exemplo:

class ContaCorrente:

    cotacao = 0.04 # Cotação do US$ # Atributo de Classe
    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite  * ContaCorrente.cotacao
        self.__saldo = saldo * ContaCorrente.cotacao

Obs. Não precisamos criar uma instância de uma classe para fazer acesso à um atributo de classe.




- Atributos Dinâmicos
  É um atributo de instância que pode ser criado em tempo de execução. Esse atributo será exclusivo da instância que o
  criou.

Exemplo:

class ContaCorrente:

    cotacao = 0.04 # Cotação do US$ # Atributo de Classe
    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite  * ContaCorrente.cotacao
        self.__saldo = saldo * ContaCorrente.cotacao

p1 = (1, 1000, 300)
p1.moeda('Real')



- Deletando Atributos
  del p1.moeda


"""



