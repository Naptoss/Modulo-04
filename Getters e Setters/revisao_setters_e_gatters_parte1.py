# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = OBTER UM VALOR(.)

class Pessoa:
    @property
    def nome(self):
        return 'Antonio'

    @nome.setter
    def nome(self, nome):
        self.atributo = nome


p1 = Pessoa()
print(p1.nome)
