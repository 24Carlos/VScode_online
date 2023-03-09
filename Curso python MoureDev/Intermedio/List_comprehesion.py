### List comprehesion ###

# Formato
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)
# transformar una lista en otra lista
# y con el range() pordemos limitarla

my_list = [i for i in range(7)]

print(my_list)

my_range = range(8)

print(list(my_range))

print(my_list)


my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)] #Multiplica los valores de la lista
print(my_list)


def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)



#create a function that convert decimal to binary
def decimal_to_binary(number):
    return bin(number)[2:]

my_list = [decimal_to_binary(i) for i in range(8)]
print(my_list)

