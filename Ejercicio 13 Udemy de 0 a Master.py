#(4)Escribir un programa que muestre el eco de todo
#lo que el usuario introduzca hasta que el usuario
#escriba “salir” que terminará.
frase=input("Escriba algo: ")
while True:
    frase=input("Vuelva a escribir algo: ")
    if frase=="Salir":
        break
