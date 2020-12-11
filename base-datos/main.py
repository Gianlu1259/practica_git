import mysql.connector

database= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="practicas"
)
#verificar si la conexion a sedo exitoza
#print(database)

#Cursor
cursor=database.cursor(buffered=True)

#Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS practicas")
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)
"""
#crear tablas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
id INT(10) auto_increment not null,
marca VARCHAR(40) not null,
modelo VARCHAR(40) not null,
precio FLOAT(10, 2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )
""")

#Insertar filas a las tablas
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Fiat', 'Palio', 25000)")

#otra manera de inserta filas a las tablas
#coches=[
#    ('Audi', 'A8', 45000),
#    ('Renault', 'Clio', 30000),
#    ('Alfa Romero', '159', 25000),
#    ('ACE', 'Genertion', 70000)
#]   
#cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
#database.commit()

#listar e imprimir datos de la base de datos
#cursor.execute("SELECT * FROM vehiculos")
#result = cursor.fetchall()
#print("---todos los coches---")
#print(result)

#Eliminar registros de la base de datos
cursor.execute("DELETE FROM vehiculos WHERE marca='Fiat'")
database.commit()
print("registros eliminados: ",cursor.rowcount )

cursor.execute("UPDATE vehiculos SET modelo='Palio' WHERE marca='Renault'")
database.commit()
print("registros actualizados: ",cursor.rowcount)




