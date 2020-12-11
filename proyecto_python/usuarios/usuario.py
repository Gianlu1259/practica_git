import datetime
import hashlib
import usuarios.conexion as conexion

conect= conexion.conectar()
database=conect[0]
cursor=conect[1]
class Usuario:
    def __init__(self, nombre, apellido, email, password):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.password=password
    
    def registrar(self):
        fecha=datetime.datetime.now()

        #cifrar contraseña
        cifrado=hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))
        sql="INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario=(self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result=[cursor.rowcount, self]
        except:
            result=[0, self]
        return result
    def identificador(self):
        sql="SELECT * FROM usuarios WHERE email=%s AND password=%s"

        #cifrar contraseña
        cifrado=hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))

        usuario=(self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        database.commit()

        result=cursor.fetchone()
        return result
