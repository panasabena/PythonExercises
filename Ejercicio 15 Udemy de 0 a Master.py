#(2) Escribir un programa que almacene las asignaturas
#de un curso (por ejemplo Matemáticas, Física, Química,
#Historia y Lengua) en una lista y la muestre por pantalla
#el mensaje Yo estudio <asignatura>, donde <asignatura>
#es cada una de las asignaturas de la lista.
materias=[]
n=int(input("Ingrese la cantidad de materias que está cursando: "))
ingrese=input("Ingrese las materias que está cursando: ")
materias.append(ingrese)
while len(materias)<n:
    ingrese=input("Ingrese las otras materias que está cursando: ")
    materias.append(ingrese)
if len(materias)==n:
    print(materias)
for i in materias:
    print("Yo estudio ",i)
    
