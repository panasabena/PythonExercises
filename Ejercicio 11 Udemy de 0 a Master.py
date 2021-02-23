#(3) Escribir un programa que pregunte al usuario su edad y muestre
#por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad=int(input("Ingrese su edad: "))
numero=0
while numero< edad:
    numero+=1
    print("Usted ha cumplido", numero, "años alguna vez")
