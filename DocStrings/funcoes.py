variavel = "Valor 1"


def soma(x, y):
    """Soma x e y

    Função de soma de valores, onde x e y serao somados

    """
    return x + y


def multiplica(x, y, z=None):
    """Multiplicacao x,y,z

    Multiplica x, y e z. O programador por omitir a variavel z caso nao
    tenha necessidade de usa-la
    """
    if z:
        return x * y
    else:
        return x * y * z


variavel_2 = 'Valor 2'
variavel_3 = 'Valor 3'
variavel_4 = 'Valor 4'
