from math import sqrt
valores=[]
elemento=input("Ingrese el valor: ")
while elemento != "":
    valores.append(float(elemento))
    elemento=input("Ingrese el siguiente valor: ")
print("Usted ingresó: ",valores)    
#desviacion estandar: (((x1-media)**2)+...+((xn-media)**2))/n
media=sum(valores)/len(valores)
print (media)
#lo que hago acá es crear una lista nueva, calculando la diferencia
#de cada valor con respecto a la media
argumento=[]
for i in (valores):
    valor=i-media
    argumento.append(valor)
#Luego aca a esos desvios de cada valor les calculo el cuadrado,
# para dejarlos postivimante orientados
#creo otra lista
cuadrados=[]
for j in argumento:
    x=j**2
    cuadrados.append(x)
  

    
#print (valores)    
print ("Desvio de cada valor:  \n" ,argumento)
print("Cuadrados de cada valor:\n" ,cuadrados)  
print("Media: ",media)

#print ("Raices:  \n",raices)
desviacion=sqrt((sum(cuadrados))/(len(valores)-1))
print("Desvio: ", desviacion)
varianza=((sum(cuadrados))/(len(valores)-1))
print("Varianza: ",varianza)
print("Cantidad de datos: ", len(valores))
