from abc import ABC, abstractclassmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numerico")
        self._valor = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor do deposito precisa ser um numero")

        self.saldo += valor

    @abstractclassmethod
    def sacar(self, valor):
        pass
