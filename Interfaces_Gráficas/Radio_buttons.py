## Radio Buttons
from tkinter import*

def mostrar ():
    if opciones.get()==1:
        label2.config(text='Has elegido Masculino')
    else:
        label2.config(text='Has elegido Femenino')

root=Tk()

opciones=IntVar()

label_1 = Label(root, text='Elige un genero')
label_1.pack()
label_1.config(bg='red')
Radiobutton(root, text='Masculino',variable=opciones, value=1,command=mostrar).pack()

Radiobutton(root, text='Femenino',variable=opciones, value=2,command=mostrar).pack()

label2=Label(root)
label2.pack()
#La siguiente linea pone de color naranja al comentario "Has elegido x genero"
label2.config(bg='orange')

root.mainloop()
