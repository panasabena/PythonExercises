#(1)Escribir un programa que almacene la cadena de caracteres
#contraseña en una variable, pregunte al usuario por la contraseña
#hasta que introduzca la contraseña correcta.

print("Ingrese una contraseña que contenga entre 8 y 12 caracteres")
contra=input("Genere su contraseña: ")
while len(contra) < 8:
    print("La contraseña no puede tener menos de 8 caracteres")
    contra=input("Genere su contraseña con más de 8 caracteres: ")
while len(contra) >12:
    print("La contraseña no puede tener más de 12 caracteres")
    contra=input("Genere su contraseña, como máximo 12 caracteres: ")
generada=input("Ingrese nuevamente su contraseña: ")

while contra != generada:
    print ("Las contraseñas deben ser iguales: ")
    generada=input("Ingrese nuevamente su contraseña: ")
else:
    print("Clave generada con éxito")
