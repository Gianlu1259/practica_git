texto=""
if(len(texto.strip())==0):
    print("la variable esta vacia")
    texto=input("ingrese valor a la variable: ")
    mayus=texto.upper()
    print(f"el valor de la variable es: {mayus}")
else:
    mayus=texto.upper()
    print(f"el valor de la variable es: {mayus}")
