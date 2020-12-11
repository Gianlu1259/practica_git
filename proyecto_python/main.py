from usuarios import acciones

print("""
Acciones disponibles:
-login
-registro
-salir
""")
accion=input("¿que desea hacer?")
hazEL=acciones.Acciones()
if accion == "login":
    hazEL.login()
elif accion=="registro":
    hazEL.registro()
else:
    print("adios")