def comprovacion(dato, tipo):
    tipo=isinstance(dato, tipo)
    resultado=""
    if (tipo):
        resultado=f"el tipo de dato:({dato}) es{type(dato)}"
        
    else:
        resultado="el tipo de dato no coinside con el valor ingresado."
    return resultado    
    

lista=["lapicera", "celular"]
texto="hola soy el texto"
entero=42959880
buleano=True
print(comprovacion(lista, list))
print(comprovacion(texto, str))
print(comprovacion(entero, int))
print(comprovacion(buleano, list))
