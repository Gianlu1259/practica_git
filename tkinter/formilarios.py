from tkinter import *

ventana=Tk()
ventana.title("Formulairos en tkinter.")
ventana.geometry("700x450")
encabezado=Label(ventana, text="Formularios de argentina")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 20),
    padx=10,
    pady=10

)
encabezado.grid(row=0, column=0, columnspan=3, sticky=W)
#poner un texto al lado de la entrada de texto
label=Label(ventana, text="nombre")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#crear entrada de texto
campo_texto= Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)


label=Label(ventana, text="apellidos")
label.grid(row=2, column=0,sticky=W, padx=5, pady=5)

campo_texto=Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="center", state="normal")


label=Label(ventana, text="descripcion")
label.grid(row=3, column=0,sticky=NW, pady=5, padx=5)

campo_grande=Text(ventana)
campo_grande.grid(row=3,sticky=W, column=1)
campo_grande.config(
    width=20,
    height=5,
    font=("Arial", 20),
    padx=5,
    pady=5

)
#crear boton
boton=Button(ventana, text="enviar")
boton.grid(row=4, column=1, sticky=E)
boton.config(
    bg="green",
    fg="red",
    padx=15,
    pady=15
)
ventana.mainloop()