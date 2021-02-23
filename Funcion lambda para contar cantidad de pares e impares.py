## Crear una funcion lambda para contar la cantidad de pares e impares

a=str(input('Quiere ingresar una lista a mano?: '))
print (a)
lista=[]
if a == 'si':
    elemento=int(input('Ingrese un numero: '))
    while elemento != '':
        lista.append(int(elemento))
        elemento=(input('Ingrese el siguiente valor:'))
    print('Usted ingresó', lista)
    cantidad_pares1=len(list(filter(lambda x:x%2 == 0, lista)))
    cantidad_impares1=len(list(filter(lambda x:x%2 != 0, lista)))
    
    print('Cantidad de números pares: ',cantidad_pares1)
    print('Cantidad de números impares: ',cantidad_impares1)

if a !='si':
    
    numeros=list(range(1,12))
    print(numeros)

    cantidad_pares=len(list(filter(lambda x:x%2 == 0, numeros)))
    cantidad_impares=len(list(filter(lambda x:x%2 != 0, numeros)))
    
    print('Cantidad de números pares: ',cantidad_pares)
    print('Cantidad de números impares: ',cantidad_impares)
