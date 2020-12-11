class coche:
    #caracteristicas del objeto
    color="rojo"
    marca="ferrari"
    modelo="aventador"
    velocidad= 300
    caballaje=500
    plaza=2
    #metodos, acciones que hace el objeto

    soy_publico="soy un atrivuto publico"
    __soy_privado="soy un atrivuto privado"

    def getPrivado(self):
        return self.__soy_privado

    def __init__(self, color, marca, modelo, velocidad, caballaje, plaza):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plaza=plaza
    def setColor(self, color):
        self.color=color
    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca=marca
    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo=modelo
    def getModelo(self):
        return self.modelo

    def setCaballaje(self, caballaje):
        self.caballaje=caballaje
    def getCaballaje(self):
        return self.caballaje

    def setPlaza(self, plaza):
        self.plaza=plaza
    def getPlaza(self):
        return self.plaza

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1
    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):
        info="---informacion del vehiculo---"
        info+="\n Color: " + self.getColor()
        info+="\n Marca: "+self.getMarca()
        info+="\n Modelo: "+self.getModelo()
        info+="\n Velocidad: "+ str(self.getVelocidad())
        info+="\n Caballaje: "+ str(self.getCaballaje())
        info+="\n Plaza: "+ str(self.getPlaza())
        return info