## Check buttom
from tkinter import *
root = Tk()
root.config(bd=20,bg='goldenrod3')
root.title('Nutricionista')

def orden():
    lista=''
    if (Paleo.get()):
        lista += "Dieta Paleolítica"
    else:
        lista += "No Paleolítica"
    if (Ceto.get()):
        lista += " y Dieta Cetogénica"
    else:
        lista += " y No Cetogénica"

    imprimir.config(text=lista)

    
Paleo=IntVar()
Ceto=IntVar()

imagen=PhotoImage(file="tenor.gif")

Label(root,image=imagen).pack(side=LEFT)

frame = Frame(root)
frame.pack(side=RIGHT)
frame.config(bg='goldenrod3')
Label(frame, text='Que dieta queres?', bg='goldenrod3', font='Curier 15').pack(anchor='w')
Checkbutton(frame, text='Quiero la Palolítica', variable=Paleo, onvalue=1, offvalue=0, bg='goldenrod3', font='Courier 10', command=orden).pack(anchor='w')
Checkbutton(frame, text='Quiero la Cetogénica', variable=Ceto, onvalue=1, offvalue=0, bg='goldenrod3', font='Courier 10', command=orden).pack(anchor='w')

imprimir=Label(frame,bg='goldenrod3')
imprimir.pack()





root.mainloop()
