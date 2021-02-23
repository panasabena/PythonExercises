## Clases y objetos
class coche: ## Creamos el molde
    def __init__(self): ## Aplicamos las caracteriisticas
        self.marca="Audi"
        self.color="Rojo"
        self.ruedas=4
        self.enmarcha=False
    def arrancar (self,arrancamos): ## Creamos un metodo
        self.enmarcha=arrancamos
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche se encuentra apagado"
    def __str__(self): ## Creamos el otro metodo
        return "Este auto es marca {}, de color {}, tiene {} ruedas".format(self.marca,self.color,self.ruedas)
micoche=coche() ## Instanciamos la clase
print(str(micoche)) ## Mostramos en pantalla
print(micoche.arrancar(False)) ##Encendemos y aoagamos el auto

