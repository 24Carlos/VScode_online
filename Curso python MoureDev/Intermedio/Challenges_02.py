### Chalanges ###


""""
    Escribe un programa que muestre por consola (con un print) los
    números de 1 a 100 (ambos incluidos y con un salto de línea entre
    cada impresión), sustituyendo los siguientes:
    Múltiplos de 3 por la palabra "fizz".
    Múltiplos de 5 por la palabra "buzz".
    Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def FizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


FizzBuzz()
print("------------------------------------")
print("Ejemplo 2")
print("------------------------------------")

"""/*
 *  Escribe una función que reciba dos palabras (String) y retorne
 *  verdadero o falso (Bool) según sean o no anagramas.
 * -Un Anagrama consiste en formar una palabra reordenando TODAS
 *  las letras de otra palabra inicial.
 * -NO hace falta comprobar que ambas palabras existan.
 * -Dos palabras exactamente iguales no son anagrama.
 */"""


def is_anagram(word_1, word_2):
    if word_1.lower() == word_2.lower():
        return False
    return sorted(word_1.lower()) == sorted(word_2.lower())


print(is_anagram("Amor", "Roma"))
print(is_anagram("moure", "eruom"))

print("------------------------------------")
print("Ejemplo 3")
print("------------------------------------")

"""/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""


def fibonacci():
    prev = 0
    next = 1
    for index in range(0, 50):
        print(f"index: {index}")
        print(f"fibonacci: {prev}")
        fib = prev + next
        prev = next
        next = fib
        if fib > 60:
            break


fibonacci()

print("------------------------------------")
print("Ejemplo 4, ¿es un primo?")
print("------------------------------------")
"""
    Escribe un programa que se encargue de comprobar si un número es o no primo.
    Hecho esto, imprime los números primos entre 1 y 100.

"""


def es_primo(num):
    if num < 2:
        return False
    if num % num == 0:
        True
    for i in range(2, num):
        if num % i == 0:
            return False
        return True
    return True


# if es_primo(int(input("Ingrese un numero: "))):
#    print("El numero es primo")
# else:
#    print("El numero no es primo")


"""/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */"""


def reverse(text):
    reverse_text = ""
    for i in range(0, len(text)):
        reverse_text += text[len(text) - i - 1]
    return reverse_text


print(reverse(input("Ingrese un texto para invertir: ")))

