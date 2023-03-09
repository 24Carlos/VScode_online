### Bucles loops y ciclos ###

#while

my_condition = 0

#while my_condition < 10:
#    print(my_condition)
    #Bucle infinito 

while my_condition < 10:
    print(my_condition)
    my_condition +=2

#if my_condition == 10:
#    print("Mi condición es igual a 10")

#⚠️ Nos acepta un else seguido de un while pero un un elif
else:
    print("Mi condición es igual o mayor que 10")


while my_condition < 20:#entramos en el while y lo sigue haciendo 22, 24 y asi 
    my_condition +=1
    if my_condition == 15:
        print("Mi condición es 15")
        print("Se detiende la ejecución")
        break
    print("Mi condición es igual o menor que 20")


#⚠️ El bucle for nos sirve para iterar una lista 

my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list: #⚠️ Elemento en la lista: imprimir(elemento de la lista)
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
for E in my_tuple:
    print(E)
print("--------------------------------")
my_dict = {"Nombre":"Carlos", "Apellido":"Gomez", "Edad":21, 1:"Python"}
for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Esto se ejecuta")
else:#⚠️ Este else pertenece al for
    print("El bucle for para mi diccionario ha finalizado")

print("--------------------------------")
print("La ejecucion continua")
#🔗 https://www.w3schools.com/python/python_while_loops.asp 🔗
#🔗 https://www.w3schools.com/python/python_for_loops.asp 🔗