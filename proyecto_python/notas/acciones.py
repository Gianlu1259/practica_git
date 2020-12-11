import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"ok {usuario[1]} vamos a crear una nota: ")
        titulo=input("ingrese el titulo de su nota: ")
        descripcion=input("ingrese la descripcion de su nota: ")

        nota=modelo.Nota(usuario[0], titulo, descripcion)
        guardar=nota.guardar() 

        if guardar[0]>= 0:
            print(f"perfecto, has guardado la nota {nota.titulo}")
        else:
            print(f"lo siento {usuario[1]}no se ah guardado la nota, algo fallo")
    
    def mostrar(self, usuario):
        print(f"vale {usuario[1]} aqui estan tus notas: ")
        nota=modelo.Nota(usuario[0])
        notas=nota.listar()

        for x in notas:
            print("**********************************************")
            print(f"titulo: {x[2]}")
            print(f"descripcion: {x[3]}")
    def borrar(self, usuario):
        print(f"\n vale {usuario[1]} vamos a borrar notas: ")
        titulo=input("ingrese el titulo de la nota que desea eliminar: ")
        nota=modelo.Nota(usuario[0], titulo)
        eliminar=nota.eliminar()

        if eliminar[0] >= 1:
            print(f"se ah eliminado la nota {nota.titulo}")
        else:
            print("algo ha fallado, intente mas tarde.")