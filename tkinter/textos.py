from tkinter import *

ventana = Tk()

ventana.geometry("500x500")

texto=Label(ventana, text="bienveidos al programa")
texto.config(
    fg="white",
    bg="black",
    font=("Consolas", 20),
)
texto.pack()

texto=Label(ventana, text="texto extra")
texto.config(
    height=3,
    bg="orange",
    font=("Arial, 18"),
    padx=40,
    pady=20,
    cursor="spider"
)
texto.pack()
ventana.mainloop()