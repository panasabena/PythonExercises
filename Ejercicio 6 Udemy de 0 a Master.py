#Nota: Ejercicios para realizar al final de la seccion.

#1: Pidele al usuario que ingrese dos numeros enteros por teclado
#y determine los siguientes aspectos.

#1: Si ambos numeros son iguales
#2: Si los numeros son diferentes
#3: Si el primero  es mayor al segundo
#4: Si el segundo es mayor al primero
numero1=int(input("Ingrese un (1) número entero: "))
numero2=int(input("Ingrese otro número entero: "))
if numero1 == numero2:
    print("Los numeros ingresados son iguales")
if numero1 != numero2:
    print("Los numeros ingresados son diferentes")
if numero1>numero2:
    print("El primer numero ingresado es mayor al segundo")
if numero2>numero1:
    print ("El segundo numero ingresado es mayor al primero")



#3: Con operadores logicos, determina si una cadena de texto ingresada por el usuario
#tiene una longitud mayor o igual a 3 y a su vez es menor a 10. (tru o false)    
print("Otro ejercicio acá adentro:")
cadena=input("Ingrese una palabra: ")
if len(cadena)>= 3 and len(cadena)<10:
    print(True)
else:
    print(False)
