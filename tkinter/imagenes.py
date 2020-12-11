from tkinter import *
from PIL import Image, ImageTk

ventana=Tk()
ventana.geometry("700x520")
Label(ventana, text="mariposa azul").pack()
imagen=Image.open("./tkinter/imagenes/mariposa.jpg")
render=ImageTk.PhotoImage(imagen)
Label(ventana, image=render).pack(anchor=W)

ventana.mainloop()