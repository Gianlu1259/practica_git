cadena=[1, 4, 2, 8, 9, 6, 5, 3]
for x in cadena:
    print(x)

cadena.sort()
print(cadena)

print(f"la longitud de la lista es: {len(cadena)}")
try:
    buscador=int(input("ingrese elemento a buscar: "))
    resultado=cadena.index(buscador)
    print(f"el numero esta en la lista, es el indice {resultado}")
except:
    print("el numero no se encuentra en la lista")
    
lista1=set(["gonzalo","alexis","pato", "tomas"])

lista2=set(["mili","mariela","buchi", "alexis"])

final= lista1 & lista2

if len(final) > 0 :
    print("hay {} elementos coincidentes".format(len(final)))
    print(final)

else:
    print("no hay repeticiones")


