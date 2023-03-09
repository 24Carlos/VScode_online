### sets ###

# viernes 6 de enero 2023

# creacion de un set que es un tipo de dato

my_set = set()
my_other_set = {}


print(type(my_set))  # con el type es un set
print(type(my_other_set))  # Nos dice que inicialmente que es un diccionario


my_other_set = {"Carlos", "Molina", 21}

print(type(my_other_set))

# operaciones con los sets


print(len(my_other_set))  # len = leng -> lognitud


# print(my_other_set[0]) #Error

my_other_set.add("fkrloss")

print(my_other_set)

# Un set no es una estructura ordenada
# lo que hace es usar un hash para meter los elementos dentro

my_other_set.add("fkrloss")
print(my_other_set)

# como segunda caracteristica un set no admite repetidos ⚠️

# Sintexis para compraobar si un elemento existe en un set ⚠️
print("fkrloss" in my_other_set)
print("carli" in my_other_set)

my_other_set.remove("fkrloss")

print(my_other_set)

# Con el clear lo que tenemos es un set vacio
my_other_set.clear()

print(len(my_other_set))


del my_other_set  # ⚠️ con esto eliminamos el objeto del set
#   NameError: name 'my_other_set' is not defined


my_set = {"Carlos", "Molina", 21}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'swift', 'python', 'JS'}


my_new_set = my_set.union(my_other_set)


print(my_new_set)
print(my_new_set.union(my_new_set))
# no se duplican porque los set no aceptan duplicados ⚠️

print(my_new_set.union(my_new_set).union({"Kotlin", "C#"}))

print(my_new_set.difference(my_set))

print(my_new_set.union(my_new_set).union({"Kotlin", "C#"}))

print(my_new_set.difference(my_set))
# ⚠️ Aca tenemos un print de que tiene solo la diferencia, a my_new_set le quitamos los elementos de  my_set

# ⚠️ Tampoco sale Kotlin ni C# porque se hizo un unicion en el print, un union temporal

#   #   #   ⚠️Referencias⚠️ #   #   #
# 🔗https://www.w3schools.com/python/python_ref_set.asp
