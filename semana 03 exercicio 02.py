class Triangulo():
    def __init__ (self, a, b, c):
        self.a, self.b, self.c = a, b, c
        
    def tipo_lado(self):
        if self.a == self.b and self.b == self.c and self.c == self.a:
            return "equilátero"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isóceles"
        else:
            return "escaleno"
            
class TestTriangulo():
    def escaleno():
        teste = Triangulo.Triangulo(1, 2, 3)
        assert teste.tipo_lado() == "escaleno"
    
    def equilatero():
        teste = Triangulo(3, 3, 3)
        assert teste.tipo_lado() == "equilátero"
    
    def isoceles():
        teste = Triangulo(3, 3, 1)
        assert teste.tipo_lado() == "isóceles"
