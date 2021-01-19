# -*- encoding: utf-8 -*-
"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

- Encapsulamento é o agrupamento de Atributos e Métodos

- Abstração expor apenas dados relevantes de uma classe, escondendo Atributos e Métodos do usuário.


"""

class Conta:
    contador = 400
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do Titular {self.__titular} com limite de {self.__limite}')

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor

    def transferir(self,valor,conta_destino):
        self.__saldo -=valor
        conta_destino.__saldo +=valor


conta1 = Conta('Renan',150,1500)
