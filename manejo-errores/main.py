#multiple exepciones
#try:
#    numero=int(input("ingrese un numero para sacar su cuadrado: "))
#    print(f"el cuadrado de {numero} es " + str(numero*numero))
#except TypeError:
#    print("debe convertir sus cadenas a enteros en el codigo")
#except ValueError:
#    print("introdusca un numero valido.")
#except Exception as e:
#    print(type(e))
#    print("el error es de tipo: ", type(e).__name__)

#exepciones personlizadas
try:
    nombre=input("ingrese nombre: ")
    edad=int(input("ingrese edad: "))
    #if edad<18 or edad>100:
    #    raise ValueError("la edad es incorrecta")
    #elif len(nombre)<1:
    #    raise ValueError("el nombre no es valido")
except Exception as e:
    print("existe un error: ", e)


        