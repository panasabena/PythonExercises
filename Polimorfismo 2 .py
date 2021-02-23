## Polimorfismo 2:
class Gato():
    def hablar(self):
        print("Miau")
class Perro(Gato):
    def hablar(self):
        print("Guau")
def escucharmascotas(animal):
        animal.hablar()
miMascota=Perro()
miMascota2=Gato()
escucharmascotas(miMascota)
escucharmascotas(miMascota2)
 
