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
        if self.a == self.b and self.b == self.c and self.c == self.a:
            return True
        else:
            return False

def test_perimetro():
    teste = Triangulo(1, 1, 1)
    assert teste.perimetro() == 3

def test_faltavalor():
    teste = Triangulo(1, 1, 0)
    assert teste.perimetro() == False

def test_retangulo():
    teste = Triangulo(3, 3, 3)
    assert teste.retangulo() == True
    

