## Creando la calculadora de Binomio cuadrado perfecto:
## Recordemos que es de la forma de aX^2+bX+c=0
from math import sqrt
a=(int(input("Ingrese el valor de a: ")))
b=(int(input("Ingrese el valor de b: ")))
c=(int(input("Ingrese el valor de c: ")))
## Formula de Bhaskara  (-b+-sqrt(b^2-4*a*c))/2*a
x1=(-b+(((b**2)-4*a*c)**.5))/2*a
x2=(-b-(((b**2)-4*a*c)**.5))/2*a
#raiz=sqrt((b**2)-4*a*c)
while type(a) ==False:
#    print("La raíz no puede ser negativa")
#    a=int(input("Ingrese nuevamente el valor de a: "))
#    b=int(input("Ingrese nuevamente el valor de b: "))
#    c=int(input("Ingrese nuevamente el valor de c: "))
print("El valor de x1 es: ",x1)    
print("El valor de x2 es: ",x2)
