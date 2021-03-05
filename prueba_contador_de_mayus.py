mayusculas=[]
pc30.review_body=['Utilicé las brocas de menor diámetro y se me doblaron varias como si fuesen de mantequilla, al hacer una mínima presión sobre ellas. Una vez dobladas, al intentar enderezarlas, se parten. Exteriormente son amarillas pero el interior es como de un fundido gris. La peor compra que he hecho en bastante tiempo.',
         'A parte de no poder elegir color, te envian el cesto de un color y el asa de otro, imagino que aprovechando los que se van rompiendo, porque dicen color aleatorio, pero en la foto, cesta y asa son del mismo color. Recomiendo comprarlo en donde se pueda elegir color. El único alivio, es que se romperá pronto, la calidad no es muy allá.']
         

cuenta=0
for c in pc30.review_body:
    #n=len(i)-1
    for i in c:
        if i.isupper():
            cuenta+=1
    mayusculas.append(cuenta)
            #j=(cuenta)
            #lista.append(j)
#n=len(lista)-1

#cantmayus=lista[n]
#mayus=[]

print(mayusculas)
