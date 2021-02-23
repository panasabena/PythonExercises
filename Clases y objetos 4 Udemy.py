## Metodos especiales:
class coche:
    def __init__(self,marca,kilometros,año):
        self.marca=marca
        self.kilometros=kilometros
        self.año=año
        print("Se ha creado un auto", self.marca)
    def __del__(self):
        print("Se ha vendido el auto", self.marca)
    def __str__(self):
        return "El auto es un {} tiene {}, y es del año {}".format(self.marca,self.kilometros,self.año)
micoche=coche("Audi",2000,1993)
print(str(micoche))
del(micoche)
        
    
