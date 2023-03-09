
### LIST ###

#Formas de crear una lista
my_list = list()

my_other_list = []


##nos calula la logitud de la lista
#print(len(my_list))


my_list = [35, 24, 62, 52, 30, 30, 17]
#lo que tenemos dentro son los elementos
#print(my_list)
#print(len(my_other_list))


my_other_list = [35, 1.77, "Brais", "Moure"]

#print(my_other_list[0])
#print(my_other_list[1])
#print(my_other_list[-1])
#print(my_other_list[-3])
#print(my_other_list[-4])
#print(my_other_list.count()) El count no es para contar los elementos, y tenemos que pasarle un valor
#print(my_list.count(30))
#Con el count retorna el numero de ocurrencias de un valor
#print(my_other_list[4])  IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list

#print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
#El problema es que si se modifica la lista original esto peta :v
#print(name)

#print(my_list + my_other_list) #agarra el contenido de una y agrega al print el contenido de la otra 
#print(my_list - my_other_list) Operación no soportada


#print(list([1, 2, 3, 4])) #Aca lo que hace es imprimir la lista que se crea ahi mismo 

print(type(my_list))

#aca lo que hace es eliminar la lista y crearlo en un string 
#El problema es que se cambie el algun trabajo en equipos y se elimine y cambie de tipo de dato
my_list = "Hola Python"

print(type(my_list))

print(my_list)

#una lista es mutable
#para agregar un elemento
my_other_list.append("MoureDev")
#con .insert(1) se pone en la posicio que tu quieras 
my_other_list.insert(1, "azul")
#con remove se eliminar un valor que se especifique 
my_other_list.remove("azul")
print(my_other_list)
my_list.remove("30")
print(my_list)


