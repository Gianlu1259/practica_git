from tkinter import *

ventana=Tk()
ventana.title("practicas")
ventana.geometry("700x400")

#crear marcos
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(bg="lightblue",
             bd=7,
             relief="raised",
             cursor="spider"   
)
marco_padre.pack(side=BOTTOM, anchor=N,fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="black",
             bd=7,
             relief="raised",
             cursor="spider"   
)
marco.pack(side=LEFT)

marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="red",
             bd=7,
             relief="raised",
             cursor="spider"   
)
marco.pack(side=RIGHT)
texto=Label(marco, text="que onda???")
texto.config(
    bg="red",
    fg="blue",
    font=("Arial", 20),
    bd=2,
    relief="solid"
)
texto.pack(anchor=CENTER, fill=Y, expand=YES)
marco.propagate(False)

ventana.mainloop()