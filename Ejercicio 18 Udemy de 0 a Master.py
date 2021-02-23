#(1) Escribir una función a la que se le pase
#una cadena <nombre> y muestre por pantalla
#el saludo ¡hola <nombre>!.
def funcion():
    nombre=input("Ingrese su nombre: ")
    print("Hola!, ", nombre)
#funcion()    

#(2) Solicitar al usuario que ingrese su dirección email.
#Imprimir un mensaje indicando si la dirección es válida o no,
#valiéndose de una función para decidirlo.
#Una dirección se considerará válida si contiene el símbolo "@".
def mail(email):
    caracterbuscado="@"
    emailValido = False
    for i in email:
        if i ==caracterbuscado:
            return True
    return False        
direccion=input("Ingrese su email: ")
if mail(direccion):
    a="Dirección válida"
    print(a)
else:
    a="Direccion inválida"
    print(a)
#    while a=="Direccion inválida":
#        direccion=input("Ingrese nuevamente su email: ")
#        for j in direccion:
#            if j == "@":
#                print("Email ingresado correctamente")            
        
