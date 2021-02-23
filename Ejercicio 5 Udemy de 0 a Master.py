#5)Aqui hay un texto que esta alreves, es un alumno, que tiene una nota
#del examen.¿Como podemos darlo vuelta y verlo normalmente?

texto = "zaid luar, 10"
def invertir_cadena_manual(texto):
    cadena_invertida = ""
    for letra in texto:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida
#print(invertir_cadena_manual(texto))
testo= "zaid luar, 10"
print('El texto es: ',testo)
testo_invertido=testo[::-1]
print('EL texto invertido es: ',testo_invertido)
