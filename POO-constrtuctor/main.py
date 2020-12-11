from coche import coche

carro = coche("negro", "ferrari", "murja", 150, 200, 4)
#carro2=coche("azul", "fiat", "palio", 200, 180, 4)
print("COCHE 1:")
print(carro.getInfo())
#print("COCHE 2:")
#print(carro2.getInfo()) 
print(carro.soy_publico)
print(carro.getPrivado())