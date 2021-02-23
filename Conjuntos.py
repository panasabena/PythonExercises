conjunto=set()
conjunto={2,"Python",True,1.0,20,"Python"}
print(conjunto)
##Vemos que cuando imprime el conjunto, el "Python" que está al final
##no lo imprime, porque no admite duplicados.
##-------------------------------------------
##Y para agregar un elemento al conjunto lo que debemos hacer es:
conjunto.add(16)
##Una vez que lo agrega, no lo  va a hacer ordenadamente, es decir al final
##Si no que "Python" lo hace a su manera.
print(conjunto)
