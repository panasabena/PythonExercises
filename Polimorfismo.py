
## Polimorfismo
## El polimorfismo, se refiere a la capacidad de tomar más de una forma
## Una operación puede tener diferentes comportamientos en diferentes instancias
## Y el comportamiento siempre depende del tipo de dato usado en la operación
## El polimorfismo es ampliamente usado en la herencia
class Persona():## Creamos al objeto
    def __init__(self):## Creamos el constructor
        self.cedula=12345
    def mensaje(self):
        print("Este mensaje viene de la clase persona")
class Obrero(Persona):
    def __init__(self):
        self.especialista=1
    def mensaje(self):
        print("Este mensaje viene de la clase Obrero")
obrero_planta=Obrero()
obrero_mensaje=Persona()
obrero_planta.mensaje()
obrero_mensaje.mensaje()

