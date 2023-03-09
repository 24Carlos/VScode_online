### Diccionarios ###

my_dict = dict()

my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Carlos", "Apellido":"Gomez", "Edad":21, 1:"Python"}

my_dict = {"Nombre":"Carlos", "Apellido":"Gomez", "Edad":21, "Lenguajes":{"Python", "Swift","Kotlin"}, 1:1.76}
#⚠️ Aca tenemos un diccionario que como clave tiene un string pero como valor tiene un set dentro
#⚠️ Esto al ser un diccionario podemos guardar datos de tupo clave : valor 


print(my_other_dict)
print(my_dict)



print(len(my_other_dict)) #En este caso tenemos 4 porque tenemos Nombre, Apellido, Edad, 1
print(len(my_dict))#En este caso tenemos 5 porque tenemos Nombre, Apellido, Edad, Lenguajes, 1



#⚠️ Esto nos muestra el valor que está almacenado en la variable nombre de my_dict
print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
#⚠️ Esta es la forma de actualizar la clave de nombre
print(my_dict["Nombre"])

print(my_dict[1])

#⚠️ Esta es una forma de agregar un nuevo campo al diccionario 
my_dict["Calle"] = "Calle fkrloss"
print(my_dict)

print("-----------")
#⚠️ Esta es una forma de eliminar algun elemento por el key 
#my_dict.pop("Calle")
#my_dict.pop("Nombre")
#my_dict.pop("Apellido")
#my_dict.pop("Lenguajes")
#my_dict.pop(1)

print(my_dict)


#⚠️comprobar si carlos eta en my_dict

#⚠️ con esto buscamos la clave en el diccionario, no le valor
print("carlos" in my_dict)
print("Apellido" in my_dict)

#⚠️ Aca obtenemos el valor en la clave Apellido
print(my_dict["Apellido"])

print("----------------------")
print(my_dict.items()) #⚠️ Nos retorna todos los valores
print("----------------------")
print(my_dict.keys()) #⚠️ Nos restorna las claves de cada valor
print("----------------------")
print(my_dict.values()) #⚠️ Nos retorna los valores de cada clave
print("----------------------")

#⚠️ Este metodo crea un diccionario nuevo sin valores #print(my_dict.fromkeys(("Nombre", 1)))

my_new_dict = my_other_dict.fromkeys(("Nombre", 1,), "Piso")
print(my_new_dict)

print("----------------------")
#💡 Creación de un diccionario desde una lista con fromkeys

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
print("----------------------")

#⚠️ Del fromkeys se le pasa un diccionario completo 
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
#⚠️ Se hace como una copia pseor solo de las claves 
print("----------------------")
#⚠️ Value nos sive para darle un valor que se repetira en todas las keys del diccionario
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print(my_new_dict)
print("----------------------")
#⚠️ No mas se pasa a una lista lo que se tiene son las claves, no el valor
#⚠️ Lista
print(list(my_new_dict.values()))
#⚠️ Tupla
print(tuple(my_new_dict))
#⚠️ Set
print(set(my_new_dict))
print("----------------------")
#⚠️ Aca nos dice que es un tipo de datos dict_values, un diccionario de valores
my_values = my_new_dict.values()
print(my_values)

#⚠️Referencias      🔗 https://www.w3schools.com/python/python_ref_dictionary.asp 🔗