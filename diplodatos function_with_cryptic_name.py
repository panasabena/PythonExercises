#def function_with_cryptic_name(n):
#    result=1
#    for x in range(1,n+1):
#        result*=x
#    return result
#print("f(5) =",function_with_cryptic_name(5))
#print("f(-5) =",function_with_cryptic_name(-5))
#print("f(-5) =",function_with_cryptic_name(-5))
n=21
result=[]
for i in range (1, n-1):
    if n % i ==0:
        continue
    result.append(i)
print("Es una lista que devuelve los restos iguales cero\nde los numeros entre 1 y n-1")
print (result)

result1=[]
for i in range (1, n-1):
    if n % i !=0:
        continue
    result1.append(i)
print("Es una lista que devuelve los restos de n (distintos de cero)\nentre los numeros entre 1 y n-1")
print (result1)

result2= [i for i in range(1,n-1) if n % i==0]
print("Osea que divide a n por cada elemento del rango entre 1 y n-1\ny devuelve la lista con la\ncondicion de que el resto sea distinto de cero")
print (result2)
print('--------------------------------------------------------------------------')
dict_with_bad_name={i: n % i
                    for i in range(1,n-1)}
result3=[]
for key, value in dict_with_bad_name.items():
    if value == 0:
        result3.append(key)
print('El tipo de dato de dict_with_bad_name es: ',type(dict_with_bad_name))
print(result3)
