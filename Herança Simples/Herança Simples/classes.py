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


class Aluno(Pessoa):  # Sub-classe
    def estudar(self):
        print(f"{self.nomeclasse} {self.nome} esta estudando...")
