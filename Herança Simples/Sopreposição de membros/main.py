from classes import *

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

c1 = Cliente("Antonio", 18)
c1.falar()
c1.comprar()
print()

c2 = ClienteVip("Ronaldo", 35, "Azul")
c2.falar()
