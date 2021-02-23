##Herencia
class Persona:
    def __init__(self,nombre,edad,apellido,sexo):
        self.nombre=nombre
        self.edad=edad
        self.apellido=apellido
        self.sexo=sexo
    def datosPersonales(self): ## Definimos un metodo
        print("El nombre de la persona es: ", self.nombre)
        print("La edad de la persona es: ", self.edad)
        print("El apellido de la persona es: ", self.apellido)
        print("El sexo de la persona es: ", self.sexo)
miPersona=Persona("Pepe",20,"Gonzalez","Masculino")
miPersona.datosPersonales()
print("\n**********Aca empieza otra persona empleada**********\n")
class Empleado(Persona): ## Creamos otra clase, y no hace falta llamar al contructor
                ## __init__, porque va a heredar todos los atributos de la clase
                ## persona. Pero como los va a heredar? Poniendo en el argumento
                ## la clase padre Empleado(Persona)
    def datosEmpleado(self, vacaciones, salario):
        print("Sus dias de vacaciones son: ", vacaciones)
        print("Su salario es: ", salario)
miPersona2=Empleado("Maria",22,"Luna","Femenino")
miPersona2.datosPersonales()
miPersona2.datosEmpleado(30,55000)
        
