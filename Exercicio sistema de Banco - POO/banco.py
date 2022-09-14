class Banco:
    def __init__(self, contas, cliente):
        self._contas = contas
        self._cliente = cliente

    @property
    def contas(self):
        return self._contas

    @property
    def cliente(self):
        return self._cliente
