class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def Presentarse(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} y mi profesion es {self.profesion}"

p = Persona("Santiago", 19, "Tatuador e Informatico")
print(p.Presentarse())  