lista=[1,2,3,4,5,6,7,8,9,10]
media=sum(lista)/len(lista)

## Esperanza es el valor i por la probabilidad de que salga ese valor i:
probabilidad_i=1/len(lista)
#media=sum(lambda x:x*probabilidad_i in lista)
print(probabilidad_i)


medianueva=[]
for i in lista:
    promedio=i*probabilidad_i
    medianueva.append(promedio)
media=(sum(medianueva))
print(media)

varianza=[]
for i in lista:
    var=(i-media)**2
    varianza.append(var)
print(sum(varianza)/len(lista))    
