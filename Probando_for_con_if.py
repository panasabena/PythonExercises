nueva=[]
lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
stop=[1,5,10,15,20]
for i in lista:
    if i not in stop:
        nueva.append(i)
print (nueva)        
