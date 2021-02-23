## Clases y objetos
class coche: ## Creamos el molde
    def __init__(self): ## Aplicamos las caracteriisticas
        self.marca="Audi"
        self.color="Rojo"
        self.__ruedas=4 ## Agregandole esos dos guiones bajos, hace que las ruedas no puedan ser cambiadas desde afuera
        self.enmarcha=False
    def arrancar (self,arrancamos): ## Creamos un metodo
        self.enmarcha=arrancamos
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche se encuentra apagado"
    def __str__(self): ## Creamos el otro metodo
        return "Este auto es marca {}, de color {}, tiene {} ruedas".format(self.marca,self.color,self.__ruedas)
micoche=coche() ## Instanciamos la clase
print(str(micoche)) ## Mostramos en pantalla
print(micoche.arrancar(False)) ##Encendemos y aoagamos el auto

print("------------------------------Otro vehiculo----------------------")
micoche2=coche()
micoche2.__ruedas=20## Observar que nosotros le estamos diciendo que el auto tiene
                    ## 20 ruedas, pero el programa no hace caso porque esta encaplsulado
                    ## para que esas 4 ruedas no sean modificadas
print(micoche2.arrancar(True))
print(str(micoche2))
