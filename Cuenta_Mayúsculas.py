string = input("Ingrese palabra: ")
indice=0
mayusculas=0
minusculas=0
while indice < len(string):
  letra = string[indice]
  if letra.isupper() == True:
    mayusculas +=1
  else:
    minusculas +=1
  indice += 1

print("Total mayusculas: " , mayusculas)
print("Total minusculas: " , minusculas)
