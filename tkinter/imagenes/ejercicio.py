from tkinter import *
from tkinter import messagebox as messageBox

ventana=Tk()
ventana.geometry("500x250")
ventana.title("Calculadora 3.000")
numero1=StringVar()
numero2=StringVar()
resultado=StringVar()

marco=Frame(ventana, width=100, height=150)
marco.config(
    bd=5,
    relief=SOLID
)
def cFloat(numero):
    try:
        result=float(numero)
    except:
        result=0
        messageBox.showerror("Error", "Error: ingrese un valor que sea valido").pack()
    return result
def sumar():
    resultado.set(cFloat(numero1.get())+cFloat(numero2.get()))
    mostrarResultado()
def restar():
    resultado.set(cFloat(numero1.get())-cFloat(numero2.get()))
    mostrarResultado()
def dividir():
    resultado.set(cFloat(numero1.get())/cFloat(numero2.get()))
    mostrarResultado()
def multiplicar():
    resultado.set(cFloat(numero1.get())*cFloat(numero2.get()))
    mostrarResultado()
def salir():
    adios=messageBox.askquestion("salir", "¿estas seguro que desea salir?")
    if adios=="yes":
        ventana.destroy()
def mostrarResultado():
    messageBox.showinfo("Resultado", f"el resultado de la ecuacion es: {resultado.get()}").pack()

marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(True)
titulo=Label(marco, text="CALCULADORA")
titulo.config(
    bg="gray",
    font=("console", 20),
    fg="black"
)
titulo.pack()
Label(marco, text="ingrese primer numero a calcular: ").pack()
Entry(marco, textvariable=numero1).pack()

Label(marco, text="ingrese segundo numero a calcular: ").pack()
Entry(marco, textvariable=numero2).pack()

Label(marco, text="opciones").pack()
Button(marco, text="sumar.", command=sumar).pack(side="right", fill=X, expand=YES)
Button(marco, text="restar.", command=restar).pack(side="right", fill=X, expand=YES)
Button(marco, text="multiplicar.", command=multiplicar).pack(side="right", fill=X, expand=YES)
Button(marco, text="dividir.", command=dividir).pack(side="right", fill=X, expand=YES)
Button(marco, text="salir.", command=salir).pack(side="right", fill=X, expand=YES)

ventana.mainloop()