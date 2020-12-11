import os
import shutil
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
    print("carpeta creada")
else:
    print("la carpeta ya existe")


#copiar carpeta
ruta="./mi_carpeta" 
ruta_nueva="./mi_carpetaCOPIADA"
#shutil.copytree(ruta, ruta_nueva)

#eliminar carpeta
os.rmdir("./mi_carpetaCOPIADA")
#ver contenido de carpeta
#print("contenido de la carpeta: ")
#contenido=os.listdir("./mi_carpeta")
#for carpeta in contenido:
#    print(carpeta)

