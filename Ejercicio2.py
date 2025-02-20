class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def Presentarse(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} y mi profesion es {self.profesion}"

class Estuadiante(Persona):
    def __init__(self, nombre, edad, profesion, grado):
        super().__init__(nombre, edad, profesion)
        self.grado = grado

    def Presentarse(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.edad}, mi profesion es {self.profesion} y mi grado es {self.grado} "   

p = Estuadiante("Santiago", 19, "Tatuador e Informatico", "HLC")
print(p.Presentarse())