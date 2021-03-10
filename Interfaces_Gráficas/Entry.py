## Interfaces gráficas:
## Entry:
from tkinter import*
## Inicia la raiz
root=Tk()
## Genera el cuadro que se ve en pantalla
frame = Frame(root, width=500, height=400)
## Se empaqueta
frame.pack()
## Genera la entrada de datos
entrada = Entry(frame)
entrada2 = Entry(frame)
entrada3 = Entry(frame)
## configura la entrada de datos:
entrada.config(justify='center', state='normal')# o puede ser state='disable' para desabilitar la celda
entrada3.config(show='*') # Esta configuración hace que la contraseña se vea con '****'
## El grid empaqueta la entrada de datos
entrada.grid(row = 0, column = 1)
entrada2.grid(row = 1, column= 1)
entrada3.grid(row = 2, column= 1)
## Genera una etiqueta en la entrada de datos, que dice "Nombre"
label = Label(frame, text= 'Nombre')
label2 = Label(frame, text= 'Apellido')
label3 = Label(frame, text= 'Contraseña')
## Empaqueta la entrada de datos
## Se le puede modificar la distancia entre las celdas con el siguiente código
#label.grid(row=0, column=0,sticky='w', padx=5, pady=5)
label.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)

## Mantiene el cuadro abierto indefinidamente, hasta que lo cerramos.
root.mainloop()
