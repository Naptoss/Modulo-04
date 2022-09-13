"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as "classes"que criam classes.
type é um metaclasse (!!!???)
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)

        if "attr_classe" in namespace:
            print(f"{name} tentou sobrescrever o atributo.")
            del namespace['attr_classe']
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = "Valor A "


class B(A):
    attr_classe_B = "Valor B "


class C(B):
    attr_classe_C = "Valor C"


b = B()
c = C()

print(c.attr_classe_C)
