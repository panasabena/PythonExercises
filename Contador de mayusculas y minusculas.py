review_body=['Malisimo',
 ',',
 'muy',
 'grande',
 'demasiado',
 'aparatoso',
 'y',
 'mal',
 'protector',
 'de',
 'pantalla']
indice=0
mayus=0
minus=0
string_general=[]
string_medio=[]
string_bajo=[]

#for i in review_body:
#    cadenas=i
#    string_bajo.append(cadenas)
#    for j in cadenas:
#        cadenas_de_cadenas=j
#        string_medio.append(cadenas_de_cadenas)
#        for k in cadenas_de_cadenas:
#            string_general.append(k)
        
#while indice < len(review_body):
#    letra = review_body[indice]
#    if letra.isupper() == True:
#        mayus += 1
#    else:
#        minus += 1
#    indice +=1     
#print((mayus))
#print((minus))

for i in review_body:
    cadenas=i
    string_bajo.append(cadenas)
    for j in cadenas:
        cadenas_de_cadenas=j
        string_medio.append(cadenas_de_cadenas)

print(string_medio)










    
