## Ejercicio 2:

##SUPONIENDO QUE LA VARIABLE ESTÁ DEFINIDA Y ES N>2:
print("Ejercicio 2\n")
n=21

dict_with_bad_name={
    i: n % i
    for i in range (1,n-1)
}
result=[]
for key, value in dict_with_bad_name.items():
    if value ==0:
        result.append(key)
print ("Lista result: ",result)

