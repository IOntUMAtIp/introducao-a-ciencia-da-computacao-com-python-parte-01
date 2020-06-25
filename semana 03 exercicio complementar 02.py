import pytest

class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
               
    def semelhantes(self, triangulo):
        triangulo01 = self.a + self.b + self.c
        triangulo02 = triangulo.a + triangulo.b + triangulo.c
        if triangulo01 > triangulo02:
            if triangulo01 % triangulo02 == 0:
                return True
            else:
                return False
        else:
            if triangulo02 % triangulo01 == 0:
                return True
            else:
                return False


def test_semelhante():
    t1 = Triangulo(2, 2, 2)
    t2 = Triangulo(4, 4, 4)
    assert t1.semelhantes(t2) is True

def test_diferente():
    t1 = Triangulo(2, 2, 2)
    t2 = Triangulo(3, 4, 4)
    assert t1.semelhantes(t2) is False
