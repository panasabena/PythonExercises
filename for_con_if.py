palabras_5=['bien',
 'calidad',
 'buena',
 '!',
 'muy',
 'precio',
 'perfecto',
 'producto',
 'buen',
 'compra',
 'perfectament',
 'genial',
 'bastant',
 'fácil',
 'recomiendo',
 'si',
 'mejor',
 'bueno',
 '...',
 'funciona',
 'pued',
 'tiempo',
 'recomend',
 'rápido',
 'cumpl',
 'perfecta',
 'bonito',
 'uso',
 'color',
 'tamaño']
palabras_4=['bien',
 'calidad',
 'buena',
 'precio',
 'producto',
 'buen',
 'bastant',
 'si',
 'muy',
 'cumpl',
 'aunqu',
 'No',
 '...',
 'perfecto',
 'pued',
 'funciona',
 'perfectament',
 '!',
 'bueno',
 'ma',
 'fácil',
 'hace',
 'tiempo',
 'compra',
 'parec',
 'por',
 'grand',
 'mejor',
 'problema',
 'uso']
palabras_3=['bien',
 'No',
 'calidad',
 'si',
 'precio',
 '...',
 'producto',
 'buena',
 'bastant',
 'aunqu',
 'ma',
 'pued',
 'mejor',
 'parec',
 'hace',
 'mal',
 'grand',
 'pequeño',
 'problema',
 'bueno',
 'por',
 'queda',
 'esperaba',
 'pero',
 'funciona',
 'cumpl',
 'demasiado',
 '!',
 'uso',
 'color']
coincide4y5=[]
for i in palabras_4:
    for j in palabras_5:
        if i==j:
            coincide4y5.append(i)
#print(len(coincide4y5))
#print(coincide4y5)        

coincide4y5con3=[]
for i in coincide4y5:
    for j in palabras_3:
        if i==j:
            coincide4y5con3.append(i)
#print(len(coincide4y5con3))
#print(coincide4y5con3)
palabras_2=['No',
 'bien',
 'calidad',
 '...',
 'si',
 'producto',
 'precio',
 'do',
 'bastant',
 'buena',
 'mal',
 'uso',
 'hace',
 'parec',
 'ma',
 'día',
 'pued',
 'solo',
 'funciona',
 'demasiado',
 'problema',
 'mejor',
 'queda',
 'pequeño',
 'pantalla',
 'foto',
 'mala',
 'part',
 'ser',
 'color']
coincide3y4y5con2=[]
for i in coincide4y5con3:
    for j in palabras_2:
        if i==j:
            coincide3y4y5con2.append(i)
#print(len(coincide3y4y5con2))            
#print(coincide3y4y5con2)
palabras_1=['No',
 'producto',
 '...',
 '!',
 'bien',
 'calidad',
 'si',
 'do',
 'día',
 'llegado',
 'recomiendo',
 'mal',
 'mala',
 'amazon',
 'dinero',
 'funciona',
 'vendedor',
 'solo',
 'pedido',
 'hace',
 'llegó',
 'muy',
 'mese',
 'despué',
 'comprar',
 'pantalla',
 'una',
 'ma',
 'recibido',
 '2']
coincide2y3y4y5con1=[]
for i in coincide3y4y5con2:
    for j in palabras_1:
        if i==j:
            coincide2y3y4y5con1.append(i)
print(len(coincide2y3y4y5con1))
print(coincide2y3y4y5con1)
