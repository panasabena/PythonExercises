#Lista de datos
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
celular=input("Ingrese su numero de celular: ")

while len(nombre)==0:
    print("Debe ingresar un nombre: ")
    nombre=input("Ingrese su nombre nuevamente: ")
while len(apellido)==0:
    print("Debe ingresar su apellido: ")
    apellido=input("Ingrese su apellido: ")
Lista=[nombre,apellido,celular]    
print ("Su nombre es "+Lista[0]+"\n" "Su apellido es "+Lista[1])
