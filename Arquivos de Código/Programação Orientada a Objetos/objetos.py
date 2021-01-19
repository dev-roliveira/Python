# -*- encoding: utf-8 -*-
"""
POO - Objetos

Objetos são Instâncias da classe, ou seja, após o mapeamento do objeto para sua representação computacional, devemos
poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de uma classe como variáveis do tipo
definido na classe.


"""


class ContaCorrente:
    contador = 4999
    def __init__(self, limite ,saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


cc1= ContaCorrente(5000, 20000)
u1 = Usuario('Renan', 'Oliveira', 'renan.oliveira', '12345')
