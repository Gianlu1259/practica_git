from tkinter import *

ventana=Tk()
ventana.geometry("600x450")
mi_menu=Menu(ventana)
ventana.config(menu=mi_menu)

archivo=Menu(mi_menu, tearoff=0)
archivo.add_command(label="nuevo archivo")
archivo.add_command(label="nuevo ventana")
archivo.add_separator()
archivo.add_command(label="abrir archivo")
archivo.add_command(label="abrir ventana")
archivo.add_separator()
archivo.add_command(label="salir", command=quit)


mi_menu.add_cascade(label="archivo", menu=archivo)
mi_menu.add_command(label="editar")
mi_menu.add_command(label="seleccionar")

ventana.mainloop()