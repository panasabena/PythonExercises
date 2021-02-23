from math import *

print("Calculadora de ecuaciones de la forma\n ax**2+bx+c=0")
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))
x1=(-b+(((b**2)-4*a*c)**.5))/2*a
x2=(-b-(((b**2)-4*a*c)**.5))/2*a
while a==False:   
    print ("Debe ingresar un valor")
    a=int(input("Ingrese el valor de a nuevamente: "))
    while a==0:
        print("El valor de a debe der distinto de cero")
        a=int(input("Ingrese el valor de a nuevamente: "))
    while ((b**2)-4*a*c) <0:
        print ("La raiz debe ser positiva")
        c=int(input("Ingrese un valor de c nuevamente: "))
print (x1,x2)    

