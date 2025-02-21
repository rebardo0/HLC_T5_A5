class Figura:
    def __init__(self):
        pass
    def calcular_area():
        pass
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return 3.14*(self.radio**2)
class Rectangulo(Figura):
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def calcular_area(self):
        return self.base*self.altura
    
c = Circulo(5)
r = Rectangulo(4, 6)
print(c.calcular_area())  # Salida esperada: 78.54 (aproximadamente)
print(r.calcular_area())  # Salida esperada: 24