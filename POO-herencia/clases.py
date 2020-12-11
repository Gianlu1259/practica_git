class Persona:
    """
    nombre
    apellido
    altura
    edad
    """
        
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre=nombre

    def getApellido(self):
        return self.apellido
    def setApellido(self, apellido):
        self.apellido=apellido

    def getAltura(self):
        return self.altura
    def setAltura(self, altura):
        self.altura=altura

    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad=edad

    def hablar(self):
        return "estoy hablando"
    def caminar(self):
        return "estoy caminando"
    def dormir(self):
        return "estoy durmiendo"


class Informatico(Persona):
    """
    lenguaje
    experiencia
    """
    def __init__(self):
        #super().__init__()
        self.lenguaje="HTML, PYTHON, CSS, JAVA"
        self.experiencia=5
    
    def aprender(self):
        self.lenguaje=lenguaje
        return self.lenguaje
    def getLenguaje(self):
        return self.lenguaje  
          
    def programar(self):
        return "estoy programando"
    def repararPC(self):
        return "repare la PC"
    
class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__()
        self.auditorRedes="experto"
        self.experiencia=5
    def auditoria(self):
        return "estoy auditando una red"

    

    