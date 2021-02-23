## Clases y objetos
class Gelatina: ## Inicializamos el molde
    def __init__(self, sabor, color, tamaño):
    ##Tenemos que crear las caracteristicas de la gelatina
    ## para eso, tenemos que crear un constructor.
    ## Un constructor nos permite inicializar las características que tenga
    ## nuestro objeto. Luego ponemos la palabra resrvada self, Self es una
    ## palabra reservada de Python, que nos permite acceder a todas las
    ## caracteristicas de nuestra clase. Luego de escribir la palabra reservada
    ## self, tenemos que poner las características de nuestro objeto.
    ## En este caso, va a ser, sabor, color, tamaño
        self.sabor=sabor
        self.color=color
        self.tamaño=tamaño
    def imprimir(self):## Es importante agregarle el metodo self, para
        ## que ingrese a nuestras caracteristicas
        print("La gelatina es de sabor "+self.sabor)
        print("La gelatina se ve de color "+self.color)
        print("La gelatina es de tamaño "+self.tamaño)
gel1=Gelatina("rojo", "frutilla", "grande")
gel2=Gelatina("verde","manzana", "mediana")
gel3=Gelatina("naranja","naranja","chica")
gel4=Gelatina("Azul", "frambuesa", "grande")
gel1.imprimir()
gel2.imprimir()
gel3.imprimir()
gel4.imprimir()
