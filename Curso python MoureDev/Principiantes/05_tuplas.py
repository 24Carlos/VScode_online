
### TUPLAS ###

my_tuple = tuple()

my_other_tuple = tuple()
#Prints para difereciar en terminal cada ejecuación
print()
print()
print("-----------------------------------")
my_tuple = (25, 1.65, "carlos", "molina", "carlos")
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))


print(my_tuple[0])

print(my_tuple[-1])

#print(my_tuple(34)) #En este caso daria un error de fuera de rango de la función

#Con las tuplas no se tienen todas las operaciones como con las lsitas

print(my_tuple.count("carlos"))

#el count como las listas, cuetas las veces que se repite

print(my_tuple.count(231))


#asi como las listas este al poner numeros negativos le da la vuelta al arrayy

#con index nos indica el indice de lo que se indiquemos, no como con las listas que no tenemos el .index()

print(my_tuple.index("carlos"))

print(my_tuple.index("molina"))

#my_tuple[1] = 1.80 esto daria error porque es inmutable y no se puede agregar, borrar, cambiar ni nada
#my_tuple[5] = 1.80, tambien daria error por la misma razón
#'tuple' object does not support item assigment

#print(my_tuple)

mst = my_tuple + my_other_tuple
print(mst)

#Aca lo que se hace es que busca esos 2 elementos concretos en las 2 tuplas, nos imprime el elemento 3 y 6
print(mst[3:6])

#para saber si se necesita mutar un "array" se piensa en usar una tupla (no se modifica) o usar una list (se puede  modificar como de la gana)







