class Contas:
    def __init__(self, agencia, id, saldo=0):
        self.agencia = agencia
        self.id = id
        self.saldo = saldo
        self.operacoes = [("DEPOSITO", saldo)]

    def saque(self, valor):
        if self.saque <= valor:
            self.saldo -= valor
            self.operacoes += [("SAQUE", valor)]
        else:
            print("Saldo Insuficiente")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes[("DEPOSITO", valor)]

    def extrato(self):
        print("Extrato CC numero %s \n" % self.numero)
        for op in self.operacoes:
            print("%10s %10.2f\n" % (op[0], op[1]))
            print("\n Saldo: %10.2f\n" % self.saldo)


class ContaPoupanca(Contas):
    pass


class ContaCorrente(Contas):
    pass
