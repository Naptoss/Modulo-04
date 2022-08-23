
from datetime import datetime
from mimetypes import init


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def pegar_ano(cls, nome, idade):
        idade = cls.ano_atual - idade
        return cls(nome, idade)


p1 = Pessoa.pegar_ano("Antonio", 18)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
