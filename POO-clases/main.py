#programacion orientada a objetos

#definir clase
class coche:
    #caracteristicas del objeto
    color="rojo"
    marca="ferrari"
    modelo="aventador"
    velocidad= 300
    caballaje=500
    plaza=2
    #metodos, acciones que hace el objeto
    def setColor(self, color):
        self.color=color
    def getColor(self):
        return self.color
    def setModelo(self, modelo):
        self.modelo=modelo
    def getModelo(self):
        return self.modelo
    def acelerar(self):
        self.velocidad+=1
    def frenar(self):
        self.velocidad-=1
    def getVelocidad(self):
        return self.velocidad
coche=coche()

coche.setColor("azul")
coche.setModelo("murcielago")

print(coche.marca, coche.getColor(), coche.getModelo())
print("velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print("velocidad nueva: ", coche.getVelocidad())

        
