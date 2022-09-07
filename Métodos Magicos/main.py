

from ast import arg
import re


class A:

    def __init__(self):
        pass

    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'Voce nao pode fazer isso'

        else:
            self.__dict__[key] = value


a = A()
a.nome = "Antonio"
a.qualquer = "Antonio2"
print(a.nome, a.qualquer)
