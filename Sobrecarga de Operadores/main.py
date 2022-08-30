"""
No python, o comportamento dos operadores é definido por metodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuario.

Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão

"""


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)

print(r1 + r2)
