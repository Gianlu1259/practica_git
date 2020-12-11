import usuarios.usuario as modelo
import notas.acciones 
class Acciones:
    def registro(self):
        print("identificate en el sistema: ")
        nombre=input("ingresa tu nombre: ")
        apellido=input("ingresa tu apellido: ")
        email=input("ingresa tu Email: ")
        password=input("ingresa tu contraseña: ")

        usuario= modelo.Usuario(nombre, apellido, email, password)
        registro=usuario.registrar()

        if registro[0]>=1:
            print(f"el usuario {registro[1].nombre} se ah registrado con el email {registro[1].email}")
        else:
            print("no te has registrado correctamente")
    def login(self):
        print("Vamos a registrarte en el sistema: ")
        try:
            email=input("ingresa tu Email: ")
            password=input("ingresa tu contraseña: ")

            usuario=modelo.Usuario("", "", email, password)
            login=usuario.identificador()

            if email == login[3]:
                print(f"Bienvenido {login[1]} te has registrado en la fecha {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto.")
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear notas     (crear)
        - Mostrar notas   (mostrar)
        - Eliminar notas  (eliminar)
        - Salir           (salir)
        """)
        accion=input("¿que deseas hacer? ")
        hazEL=notas.acciones.Acciones()
        
        if accion == "crear":
            print("vamos a crear.")
            hazEL.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion=="mostrar":
            print("notas actuales:")
            hazEL.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion=="eliminar":
            print("que nota desea eliminar?")
            hazEL.borrar(usuario)
            self.proximasAcciones(usuario)
        else:
            print(f"Adios {usuario[1]} nos vemos")
            exit()
        