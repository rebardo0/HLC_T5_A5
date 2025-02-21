class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def Presentarse(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} y mi profesion es {self.profesion}"

class Trabajador(Persona):
    def __init__(self, nombre, edad, profesion, empresa):
        super().__init__(nombre, edad, profesion)
        self.empresa = empresa

    def Presentarse(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.edad}, mi profesion es {self.profesion} y mi empresa es {self.empresa} "   

p = Trabajador("Santiago", 19, "Tatuador e Informatico", "La sopa de alberta")
print(p.Presentarse())