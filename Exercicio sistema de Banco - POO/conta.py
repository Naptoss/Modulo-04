
from abc import ABC, abstractclassmethod


class Conta:
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia} '
              f'Conta: {self.conta} '
              f'Saldo: {self.saldo}')

    @abstractclassmethod
    def sacar(self, valor): pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print("Valor insuficiente")
            return

        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=10):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo Insuficiente")
            return

        self.saldo -= valor
        self.detalhes()
