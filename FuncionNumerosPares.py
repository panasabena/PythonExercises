#(4) Crea una funcion que nos devuelva numeros pares.
def generapares(limite):
    num=1
    lista=[]
    while num<limite:
        lista.append(num*2)
        num=num+1
    return lista
print(generapares(int(input("Ingrese un numero: "))))
