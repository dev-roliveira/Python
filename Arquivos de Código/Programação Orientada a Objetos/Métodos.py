# -*- encoding: utf-8 -*-

"""
POO - Métodos

- Métodos representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos em 2 grupos: Métodos de Instância ou Método de Classe.

- Método de Instância
  O método __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe.
  Os métodos dunder em Python são chamados de "Métodos Mágicos".
  Ele trabalha com valores da Instância do Objeto

Exemplo:
class ContaCorrente:
    contador = 0

    def __init__(self, numero, limite, saldo):
        self.__id = ContaCorrente.contador + 1
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__id

    def Cambio(self):
        Retorna o Cambio do Cliente para US$
        return self.__saldo / 5.20

c1 = ContaCorrente(1, 1300, 4000)
print(c1.Cambio())

Exemplo 2


from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self,senha):
        if cryp.verify(senha,self.__senha):
            return True
        return False

- Métodos de Classe(Estáticos)
  Não estão vinculados em nenhuma instância da classe, mas sim diretamente à ela.
  Uma diferença nos Métodos de Classe em relação aos Atributos de Classe é que na declaração desses métodos utiliza-se um
  decorator para indicar que o método é de Classe e não de Instância.


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self,senha):
        if cryp.verify(senha,self.__senha):
            return True
        return False


- Métodos de Classe x Instância
  Cria-se métodos de instância quando esses métodos precisam fazer acesso à atributos.
  Em métodos de classe, o acesso é à classe


- Método Privado
  Usa-se __ antes do nome.
  Exemplo
  def __usuario(self):


- Métodos Estáticos
  Não tem acesso à classe e nem à instância.

Exemplo:
@staticmethod
def definicao():
    return 'TESTE'

"""