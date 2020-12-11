import sqlite3

conexion = sqlite3.connect("/home/gianluca/Escritorio/practicas/base-datos/My_base.db")
cursor=conexion.cursor()

#instruccionSQL="CREATE TABLE usuario(id INTEGER PRIMARY KEY AUTOINCREMENT,"+ "nombre VARCHAR(30),"+"apellido VARCHAR(50)"+")"
#cursor.execute(instruccionSQL)

#instruccionSQL="INSERT INTO usuario VALUES(null, 'Ornella', 'pastore')"
#cursor.execute(instruccionSQL)
#conexion.commit()

#borrar datos
#cursor.execute("DELETE FROM usuario")
#conexion.commit()


#insertar muchos registros de golpe

#usuario = [
#    ("Gianluca", "Pastore"),
#    ("Nicole", "ferreira"),
#    ("Ornella", "Gomez"),
#    ("Gustavo", "Cabrera"),
#]
#cursor.executemany("INSERT INTO usuario VALUES(null, ?, ?)", usuario)
#conexion.commit()

#cambiar datos
cursor.execute("UPDATE usuario SET apellido='Pastore' WHERE apellido='Cabrera'")
conexion.commit()

#listar datos
cursor.execute("SELECT * FROM usuario")
usuarios=cursor.fetchall()
for x in usuarios:
    print(f"id: {x[0]}")
    print(f"nombre: {x[1]}")
    print(f"apellido: {x[2]}")
    print("\n")
conexion.close()