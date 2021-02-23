## Herencia Multiple:
class Clase1:
    def saluda(self):
        print("Hola soy el metodo de la clase uno")
class Clase2:
    def metodo2(self):
        print("Hola soy el metodo de la clase dos")
class Clase3(Clase1,Clase2):
    def metodo3(self):
        print("Hola soy el metodo de la clase tres")
c=Clase3()
c.metodo2()
c.saluda()
c.metodo3()
