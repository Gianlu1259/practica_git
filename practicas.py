contador=1
aprobados=0
suspendids=0
cantidad_alumnos=int(input("ingresar cantidad de alumnos: "))
cantidad_alumnos+=1
while(contador!=cantidad_alumnos):
    notas=int(input(f"ingrese la nota del \"alumno {contador}\": "))
    if(notas>= 7 and notas<=10):
        aprobados+=1
    elif(notas>=0 and notas<=7):
        suspendids+=1
    contador+=1
print(f"la cantidad de aprobados son: {aprobados} y la cantidad de suspendidos es: {suspendids}")