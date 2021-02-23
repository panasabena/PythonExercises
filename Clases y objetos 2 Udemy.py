## Clases y objetos:
class Persona:
    def __init__(self,nombre, edad, sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    def datosPersonales(self):
        print("El nombre de la persona es: ", self.nombre)
        print("La edad de la persona es: ", self.edad)
        print("El sexo de la persona es: ", self.sexo)
miPersona=Persona("Roberto", 20,"Masculino")
miPersona2=Persona("Pamela", 30, "Femenino")
miPersona3=Persona("Alfredo",26,"Masculino")

miPersona.datosPersonales()
miPersona2.datosPersonales()
m
iPersona3.datosPersonales()
