from pydoc import cli
from classes import Cliente, Endereco

cliente1 = Cliente("Luiz", 32)
cliente1.insere_endereco("João Pessoa", "PB")
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente("Maria", 55)
cliente2.insere_endereco("Salvado", "BA")
cliente2.insere_endereco("Rio de Janeiro", "RJ")
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente("Joao", 19)
cliente3.insere_endereco("Natal", "RN")
cliente3.insere_endereco("Fortaleza", "CE")
cliente3.insere_endereco("Manaus", "AM")
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()
