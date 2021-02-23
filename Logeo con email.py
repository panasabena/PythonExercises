print("LOGEO DE CUENTA")
contador=0
email=False
miEmail=input("Introduce tu e-mail: ")
for i in miEmail:
    if (i=="@"):
        contador=contador+1
    if contador == 1:
        print("El email es correcto")
    while contador ==0:
        print ("El e-mail ingresado no es valido")
    miEmail=input("Introduce tu e-mail nuevamente : ")

