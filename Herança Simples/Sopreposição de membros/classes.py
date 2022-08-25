class Pessoa:       # Superclasse
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeclasse} {self.nome} esta falando...")


class Cliente(Pessoa):  # Sub-classe
    def comprar(self):
        print(f'{self.nomeclasse} {self.nome} esta comprando...')

    def falar(self):
        print("ESTOU EM CLIENTE")


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
        
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f"{self.nome} {self.sobrenome}")
