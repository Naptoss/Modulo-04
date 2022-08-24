from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever


escritor = Escritor("Antonio")
caneta = Caneta("Bic")
maquina = MaquinaDeEscrever()

# print(escritor.nome)
# print(caneta.marca)

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
