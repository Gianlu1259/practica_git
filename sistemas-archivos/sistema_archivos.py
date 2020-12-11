from io import open
import pathlib
import shutil
import os
import os.path
ruta=str(pathlib.Path().absolute()) + "/fichero_texto.txt" 
archivo=open(ruta, "a+")
archivo.write("***que ondaa***\n")
archivo.close()

archivo_lectura=open(ruta, "r")
contenido=archivo_lectura.read()
#print(contenido)

lista=archivo_lectura.readlines()
archivo_lectura.close()
for elemento in lista:
    print("- " + elemento.center(25))

#copiar
#ruta_nueva=str(pathlib.Path().absolute()) + "/fichero_copiado.txt" 
ruta_alternativa=str(pathlib.Path().absolute()) + "/carpeta_pruebas/fichero_copiado77.txt"
#shutil.copyfile(ruta, ruta_alternativa)

#mover archivo
#ruta=str(pathlib.Path().absolute()) + "/fichero_texto.txt" 
#ruta_alternativa=str(pathlib.Path().absolute()) + "/carpeta_pruebas/fichero_copiado77.txt"
#shutil.move(ruta_alternativa, ruta)

#eliminar archivo
#os.remove(ruta_alternativa)

#verificar si existe un archivo
#print(os.path.abspath("./"))
ruta_comprobar=os.path.abspath("./") + "/fichero_texto.txt"
ruta_comprobar="./fichero_texto.txt"
print(ruta_comprobar)
if os.path.isfile(ruta_comprobar):
    print("el achivo existe")
else:
    print("el archico no existe")