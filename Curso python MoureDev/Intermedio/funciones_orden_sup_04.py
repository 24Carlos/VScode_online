### Funciones de orden superior ###


from functools import reduce
import random


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_value_and_add_random_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_value_and_add_random_value(5, 2, sum_one))
print(sum_two_value_and_add_random_value(5, 2, sum_five))

chatgtp = """
# -------------------------------------------------------------------------
# Multiplicar cada elemento de una lista por 2 usando map()
def multiplicar_por_dos(x):
    return x * 2


lista = [1, 2, 3, 4, 5]
resultado = map(multiplicar_por_dos, lista)
print(list(resultado))  # salida: [2, 4, 6, 8, 10]
# -------------------------------------------------------------------------
# Filtrar los números pares de una lista usando filter()


def es_par(x):
    return x % 2 == 0


lista = [1, 2, 3, 4, 5]
resultado = filter(es_par, lista)
print(list(resultado))  # salida: [2, 4]

# -------------------------------------------------------------------------
# Calcular la suma de una lista usando reduce()


def sumar(x, y):
    return x + y


lista = [1, 2, 3, 4, 5]
resultado = reduce(sumar, lista)
print(resultado)  # salida: 15
"""

### CLOSURES ###


def sum_ten():
    # va a recibir cuanto la vamos a sumar y dentro seguirá
    def add(value):
        return value + 10
    #! definimos dentro de una función otra función que va a hacer algo
    return add
    #! podemos retornar funciones
    #! tenemos la llamada a la función sun_ten() y dentro se ejecuta se ejecuta el codigo
    #! que pertenece a una función


add_closure = sum_ten()
print(add_closure)  # * Imprime <function sum_ten.<locals>.add at 0x100c4ad40>
print(add_closure(5))  # * Imprime 15


def sum_ten_2(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure_2 = sum_ten_2(5)
print(add_closure_2(5))  # * imprime 20


sum_ten_2(5)(1)  # * imprime 20

### Funciones de orden superior integradas ###
# * a cada uno de los numeros de la lista se le multiplicar x2
# map
numbers = [2, 5, 10, 21]


def multi_2(number):
    return number * 2


print(map(multi_2, numbers))  # *imprime el objeto
print(list(map(multi_2, numbers)))  # * imprime [4, 10, 20, 42]


# * Filter
def filter_greater_than_ten(number):
    if number > 10:
        return True
    else:
        return False


# * imprime 21, que es el unico que tenemos mayour que 10
print(list(filter(filter_greater_than_ten, numbers)))
# * tenemos lo mismo pero con una lambda, no es necesario crear una función aparte
print(list(filter(lambda number: number > 10, numbers)))

print("Reduce")
#! Reduce
numbers = [2, 5, 10, 21, 3, 30]


def sum_2_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value


print(reduce(sum_2_values, numbers))
###
