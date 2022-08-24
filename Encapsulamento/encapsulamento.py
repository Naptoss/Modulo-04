"""
public, protected, private

_ - Protected

__ - Privado


"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Antonio')
bd.inserir_cliente(2, 'Allyson')
bd.inserir_cliente(3, 'Sammy')
bd.inserir_cliente(4, 'Theo')
