from tkinter import *
from tkinter import ttk

ventana=Tk()
ventana.minsize(500, 500)
ventana.title("Proyecto Tkinter")
ventana.resizable(0, 0)

#crear pantallas de menu
def home():
    inicio_label.config(
        bg="yellow",
        fg="blue",
        font=("console", 20),
        pady=20,
        padx=20
    )
    inicio_label.grid(row=0, column=0)

    productos_box.grid(row=1, column=0)

    #mostrar productos en pantalla
    """
    for product in products:
        if len(product)==3:
            product.append("added")
            Label(productos_box, text=product[0]).grid()
            Label(productos_box, text=product[1]).grid()
            Label(productos_box, text=product[2]).grid()
            Label(productos_box, text="------------------------").grid()
    """
    for product in products:
        if len(product)==3:
            product.append("added")
            productos_box.insert("", 0, text=product[0], values=(product[1]))
    #ocultar otras pantallas al cargar esta
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    return True

def add():
    #Encabezado
    add_frame.grid(row=1)
    add_label.config(
        bg="yellow",
        fg="blue",
        font=("console", 20),
        pady=20,
        padx=80
    )
    add_label.grid(row=0, column=0, columnspan=4)
    #campos de formularios
    add_name_label.grid(row=1, column=0)
    add_name_entry.grid(row=1, column=1, sticky=W)

    add_price_label.grid(row=2, column=0, sticky=W)
    add_price_entry.grid(row=2, column=1, sticky=W)

    add_descripcion_label.grid(row=3, column=0, sticky=NW)
    add_descripcion_entry.grid(row=3, column=1, sticky=W)

    boton.grid(row=4, column=1)
    boton.config(
        bg="black",
        fg="red",
        pady=5,
        padx=10
    )

    add_label.grid(row=0, column=0)
    #ocultar otras pantallas al cargar esta
    info_label.grid_remove()
    inicio_label.grid_remove()
    productos_box.grid_remove()
    return True

def info():
    info_label.config(
        bg="yellow",
        fg="blue",
        font=("console", 20),
        pady=20,
        padx=20
    )
    info_label.grid(row=0, column=0)
    #ocultar otras pantallas al cargar esta
    add_label.grid_remove()
    add_frame.grid_remove()
    inicio_label.grid_remove()
    productos_box.grid_remove()
    return True

def add_productos():
    products.append([
        name_data.get(),
        price.get(),
        add_descripcion_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price.set("")
    add_descripcion_entry.delete("1.0", END)
    home()

#definir campos de pantalla (INICIO)
inicio_label=Label(ventana, text="Inicio")
#productos_box=Frame(ventana, width=250)
#Label(productos_box).grid(row=0)

productos_box=ttk.Treeview(height=12, column=2)
productos_box.grid(row=1, column=0, columnspan=2)
productos_box.heading("#0", text="Producto", anchor=W)
productos_box.heading("#1", text="Precio", anchor=W)

#definir campos de pantalla (AÑADIR)
add_label=Label(ventana, text="Añadir producto")
#añadir campos de pantalla (INFO)
info_label=Label(ventana, text="Informacion")

products=[]
name_data=StringVar()
price=StringVar()

#campo de formularios
add_frame=Frame(ventana)

add_name_label=Label(add_frame, text="Nombre del producto: ")
add_name_entry=Entry(add_frame, textvariable=name_data)

add_price_label=Label(add_frame, text="Precio del producto:")
add_price_entry=Entry(add_frame, textvariable=price)

add_descripcion_label=Label(add_frame, text="Descripcion:")
add_descripcion_entry=Text(add_frame)
add_descripcion_entry.config(
    width=30,
    height=15,
    pady=15,
    padx=15
)

boton=Button(add_frame, text="Guardar", command=add_productos)

#crear menu
menu_principal=Menu(ventana)
home()

menu_principal.add_command(label="Inicio", command=home)
menu_principal.add_command(label="Añadir", command=add)
menu_principal.add_command(label="Informacion", command=info)
menu_principal.add_command(label="Salir", command=ventana.quit)

ventana.config(menu=menu_principal)



ventana.mainloop()