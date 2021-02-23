## Creando mi primer programa
class alimentos:
    def __init__(self,Grupo,nombre,calorias):#,Grupo4,Grupo5,Grupo6,Grupo7):
        self.Grupo=Grupo
        self.nombre=nombre
        self.calorias=calorias
        #self.Grupo4=Grupo4
        #self.Grupo5=Grupo5
        #self.Grupo6=Grupo6
        #self.Grupo7=Grupo7
        #print("Se ha creado un alimento ",self.Grupo,nombre,calorias)
    def __str__(self):
        return "El alimento es del grupo {}, es un/a {} y tiene {} calorías".format(self.Grupo,self.nombre,self.calorias)
aliingr=alimentos(int(input("Ingrese el N° de grupo de su alimento: ")),input("Ingrese el alimento que comió: "),input("tiene x calorias: "))        
print(str(aliingr))
