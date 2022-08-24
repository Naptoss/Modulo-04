class A:
    vc = 123

    def __init__(self):
        self.vc = 321


a1 = A()
a2 = A()

A.vc = "Alterado"

# print(a1.__dict__) # primeiro o python vai procurar na instancia se a classe  a1.vc existe, se ela nao existe ele vai procurar direto na classe
# print(a2.__dict__)
# print(A.__dict__)
# print()

print(a1.vc)
print(a2.vc)
print(A.vc)
