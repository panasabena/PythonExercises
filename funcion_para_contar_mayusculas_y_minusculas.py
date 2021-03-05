## Crear una funcion para contar las mayúsculas y minúsculas
def contador_minusculas_mayusculas(cadena):
    contador={'minusculas': 0, 'mayusculas': 0}
    for c in cadena:
        if c.isupper():
            contador['mayusculas']+=1
        elif c.islower():
            contador['minusculas']+=1
    return contador
frase='Python es un lenguaje de programacion'
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
print(contador_minusculas_mayusculas(review_body))
