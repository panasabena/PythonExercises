#(3) Escribir un programa que pregunte al usuario su nombre,
#edad, dirección y teléfono y lo guarde en un diccionario.
#Después debe mostrar por pantalla el mensaje <nombre> tiene
#<edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
nombre=input("Cómo es tu nombre?: ")
edad=input("Cuántos años tenes?: ")
direccion=input("Cuál es tu dirección?: ")
telefono=input("Cuál es tu teléfono?: ")

persona={"Nombre: ":nombre,"Años: ":edad,"Dirección: ":direccion,"Teléfono: ":telefono}

#print("Su nombre es: ",persona["nombre"], " tiene ",persona["edad"]," años", " vive en ", persona["direccion"], " y su número de teléfono es ", persona["telefono"])
#print(nombre)
