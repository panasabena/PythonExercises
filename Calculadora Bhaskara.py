## Creando la calculadora de Binomio cuadrado perfecto:
## Recordemos que es de la forma de aX^2+bX+c=0
from math import sqrt
a=(int(input("Ingrese el valor de a: ")))
b=(int(input("Ingrese el valor de b: ")))
c=(int(input("Ingrese el valor de c: ")))
## Formula de Bhaskara  (-b+-sqrt(b^2-4*a*c))/2*a
def raiz(a,b,c):
    try:
        return sqrt((b**2)-4*a*c)
    except:
        print("La raiz no puede ser negativa")
        
print("La raiz es: ",raiz(a,b,c))        
