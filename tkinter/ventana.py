#Tkinter
#modulo para crear interfezes graficas de usuario
from tkinter import *
import os.path
class Programa:
    def __init__(self):
        self.title="interfaz grafica"
        self.size="750x450"
        self.resizable=False
    def cargar(self):
        #crear ventana raiz
        ventana= Tk()
        self.ventana=ventana
        #titulo de la ventana
        ventana.title(self.title)

        #icono de la ventana
        #ventana.iconbitmap("./tkinter/imagenes/logo.ico")

        #definir el tamaño de la ventana
        ventana.geometry(self.size)

        #bloquear tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)
        
    def addTexto(self):
        texto=Label(self.ventana, text="Bienvenidos a BUHO")
        texto.pack()
    def mostrar(self):
        #arrancar y mostrar ventana hasta que decida cerrarla
        self.ventana.mainloop()
programa= Programa()
programa.cargar()
programa.addTexto()
programa.mostrar()