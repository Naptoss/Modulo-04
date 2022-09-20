"""O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python."""


from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    @property
    def nome_e_idade_completo(self):
        return f"{self.nome} {self.sobrenome} tem {self.idade} "


p1 = Pessoa("Antonio", "Gabinio", 18)

print(p1.nome_e_idade_completo)
