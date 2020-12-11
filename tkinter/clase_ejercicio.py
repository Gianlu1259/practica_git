from tkinter import messagebox 
from tkinter import *
class Calculos:
    def __init__(self, alertas):
        self.numero1=StringVar()
        self.numero2=StringVar()
        self.resultado=StringVar()
        self.alertas=alertas

    def cFloat(self, numero):
        try:
            result=float(numero)
        except:
            result=0
            self.alertas.showerror("Error", "Error: ingrese un valor que sea valido").pack()
        return result
    def sumar(self):
        self.resultado.set(self.cFloat(self.numero1.get())+self.cFloat(self.numero2.get()))
        self.mostrarResultado()
    def restar(self):
        self.resultado.set(self.cFloat(self.numero1.get())-self.cFloat(self.numero2.get()))
        self.mostrarResultado()
    def dividir(self):
        self.resultado.set(self.cFloat(self.numero1.get())/self.cFloat(self.numero2.get()))
        self.mostrarResultado()
    def multiplicar(self):
        self.resultado.set(self.cFloat(self.numero1.get())*self.cFloat(self.numero2.get()))
        self.mostrarResultado()
    def salir(self):
        adios=self.alertas.askquestion("salir", "¿estas seguro que desea salir?")
        if adios=="yes":
            ventana.destroy()
    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"el resultado de la ecuacion es: {self.resultado.get()}").pack()
        #self.numero1.set("")
        #self.numero2.set("")

ventana=Tk()
ventana.geometry("700x400")
ventana.title("Calculadora 3.000")

marco=Frame(ventana, width=700, height=400)
marco.config(
    bd=5,
    relief=SOLID
)

marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(True)
titulo=Label(marco, text="CALCULADORA")
titulo.config(
    bg="gray",
    font=("console", 20),
    fg="black"
)
titulo.pack()

calculadora=Calculos(messagebox)
Label(marco, text="ingrese primer numero a calcular: ").pack()
Entry(marco, textvariable=calculadora.numero1).pack()

Label(marco, text="ingrese segundo numero a calcular: ").pack()
Entry(marco, textvariable=calculadora.numero2).pack()

Label(marco, text="opciones").pack()
Button(marco, text="sumar.", command=calculadora.sumar).pack(side="right", fill=X, expand=YES)
Button(marco, text="restar.", command=calculadora.restar).pack(side="right", fill=X, expand=YES)
Button(marco, text="multiplicar.", command=calculadora.multiplicar).pack(side="right", fill=X, expand=YES)
Button(marco, text="dividir.", command=calculadora.dividir).pack(side="right", fill=X, expand=YES)
Button(marco, text="salir.", command=calculadora.salir).pack(side="right", fill=X, expand=YES)

ventana.mainloop()
