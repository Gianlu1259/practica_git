from tkinter import *
from tkinter import messagebox as messageBox
ventana=Tk()
ventana.config(
    bd=70
)
def mostrarAlerta():
    messageBox.showinfo("alerta", "hola gianluca")
def salir(nombre):
    resultado=messageBox.askquestion("salir", "estas seguro que deseas salir?")
    if resultado =="yes":
        messageBox.showinfo("salir", f"adios {nombre}")
        ventana.destroy()
Button(ventana, text="mostrar alerta", command=mostrarAlerta).pack()
Button(ventana, text="salir", command=lambda:salir("gianluca")).pack()
ventana.mainloop()