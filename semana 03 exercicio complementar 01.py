class Triangulo():
    def __init__ (self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        if self.a == 0 or self.b == 0 or self.c == 0:
            return False
        else:
            perimetro = self.a + self.b + self.c
            return perimetro

    def retangulo(self):
        if self.c ** 2 == self.a ** 2 + self.b ** 2:
            return True
        else:
            return False

import pytest

@pytest.mark.parametrize("a, b, c, saida", [(3, 3, 3, 9),
                                            (2, 2, 2, 6)])

def test_perimetro(a, b, c, saida):
    c = Triangulo(a, b, c)
    assert c.perimetro() == saida

@pytest.mark.parametrize("a, b, c, teste", [(3, 4, 5, True)])

def test_retangulo(a, b, c, teste):
    d = Triangulo(a, b, c)
    assert d.retangulo() == teste
