##      Excepciones     ###
### manejo de erroes ###

n1 = 5;
n2 = 1;
n2 = "1"

try:
    print(n1 + n2);
    print("No se ha producido error 🧐")
except:
    print("Error! 💀 except")
    #Esta linea se ejecuta si en el try y except hay error. 🤙
else:
    print("La ejecucion continua 🤙 else")
    #Esta linea se ejecuta si no hay errores 😢
finally:
    print("La ejecución continua 🫔 finally")
    #Esta linea se ejecuta siempre, haya o no error 🤔
#🔷 Siempre debe haber un try / except, el else y finally es opcional 
print("------------------------")

#⚠️ Excepciones por tipo

try:
    print(n1 + n2)
except TypeError: # este se ejecuta solo si hay un TypeError 
    print("Se ha producido un TypeError!!! 💀")
except ValueError:
    print("Se ha producido un ValueError!!! 💀")
print("------------------------")
print("------------------------")


# Captura de la información de la excepción. 
try:
    print(n1 + n2)
    print("No se ha producido un error")
except TypeError as error: # Aca tenemos la captura del error en una variable 
    print(f"La excepcion es: [{error}]")
print("------------------------")
print("------------------------")






#🔗 https://www.w3schools.com/python/python_try_except.asp 