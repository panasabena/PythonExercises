#para notas intente' hacer una salvacion de error, pero por el momento
#no me salio'pero el programita anda
notas=(1,2,3,4,5,6,7,8,9,10)
nota=int(input("Ingrese el valor de la nota:"))
def evaluacion (nota):
    notas=(1,2,3,4,5,6,7,8,9,10)
    valoracion="Aprobado"
    if nota <5:
        valoracion="Desaprobado"
    return valoracion
print(evaluacion(nota))
