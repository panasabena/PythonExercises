## Creando funciones:
def suma():
    x=int(input("Ingrese un valor: "))
    y=int(input("Ingrese el segundo valor: "))
    j=int(input("Ingrese el tercer valor: "))
    resultado=x+y+j
    promedio=(x+y+j)/3
    print("La suma de los dos valores es: ",resultado)
    print("El promedio de los valores ingresados es: ",promedio)
#suma()
##Creando funciones con varios argumentos:
def suma2(num1,num2,num3):
    #num1=int(input("Ingrese el primer valor: "))
    #num2=int(input("Ingrese el segundo valor: "))
    #num3=int(input("Ingrese el tercer valor: "))
    suma=num1+num2+num3
    print("La suma de los tres valores ingresados es: ", suma)
    return suma
print(suma2(4,5,6))    
    

    
