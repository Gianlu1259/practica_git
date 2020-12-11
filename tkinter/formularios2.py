from tkinter import *

ventana=Tk()
ventana.geometry("700x500")
encabezado = Label(ventana, text="formulrio 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("console", 20)
)
encabezado.grid(row=0, column=0, columnspan=5,sticky=NW)

def mostrarProfecion():
    texto=""
    if wed.get():
        texto+="desarroyo wed.com"
    if movil.get():
        if wed.get():
            texto+=" y desarroyo movil.com"
        else:
            texto+="desarroyo movil.com"
    mostrar.config(text=texto)

#checkbutton
wed=IntVar()
movil=IntVar()
Label(ventana, text="¿a que te dedicas?").grid(row=1, column=0, sticky=NW)
Checkbutton(
    ventana,
    text="desarroyo wed",
    variable=wed,
    onvalue=1,
    offvalue=0,
    command=mostrarProfecion
).grid(row=3, column=0, sticky=NW)

Checkbutton(
    ventana,
    text="desarroyo movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfecion   
).grid(row=4, column=0, sticky=NW)

mostrar=Label(ventana)
mostrar.grid(row=5, column=0)

#radiobutton
opcion=StringVar()
opcion.set(None)

def mostrarGenero():
    marcado.config(text=opcion.get())

Radiobutton(
    ventana,
    text="masculino",
    value="masculino",
    variable=opcion,
    command=mostrarGenero
).grid(row=6, column=0, sticky=W)
Radiobutton(
    ventana,
    text="femenino",
    value="femenino",
    variable=opcion,
    command=mostrarGenero
).grid(row=7, column=0, sticky=W)

marcado=Label(ventana)
marcado.grid(row=8, column=0, sticky=W)

#opcion menu
def seleccion():
    seleccionado.config(text=opcion.get())

opcion=StringVar()
opcion.set("opcion 1")

select=OptionMenu(ventana, opcion, "opcion1", "opcion2", "opcion3")
select.grid(row=6, column=2)
Button(ventana, text="ver opcion", command=seleccion).grid(row=8, column=2)

seleccionado=Label(ventana)
seleccionado.grid(row=9, column=2)
ventana.mainloop()

