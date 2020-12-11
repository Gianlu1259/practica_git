from tkinter import *

ventana=Tk()
ventana.geometry("700x450")

def getDato():
    resultado.set(dato.get())
    if len(resultado.get())>=1:
        dato_recogido.config(
        bg="red",
        fg="blue"
        )
dato=StringVar()
resultado=StringVar()
Label(ventana, text="ingrese dato").pack()
Entry(ventana, textvariable=dato).pack()

Label(ventana, text="dato recogido").pack()
dato_recogido=Label(ventana, textvariable=resultado)

dato_recogido.pack()

Button(ventana, text="mostrar dato", command=getDato).pack()

ventana.mainloop()