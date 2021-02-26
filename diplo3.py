## Ejercicio 3:

## SUPONIENDO QUE n>2:
print("Ejercicio 3:\n")
n=21

result=[]

for i in range (1, n-1):
    if n % i !=0:
        continue
    result.append(i)
print(result)    
