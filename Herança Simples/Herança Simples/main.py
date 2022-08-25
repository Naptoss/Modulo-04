from classes import *

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

c1 = Cliente("Antonio", 18)
c1.falar()
c1.comprar()
print()

a1 = Aluno("Sammy", 25)
a1.falar()
a1.estudar()
print()

p1 = Pessoa("Allyson", 17)
p1.falar()
print()
