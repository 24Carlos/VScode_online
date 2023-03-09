"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""

import random
import string
# Funcion para colocar el True o false
# si le coloca alguno otro caracter o un "N" o "n" se colocará en false por defceto


def true_false(opc):
    if opc == "Y" or opc == "y":
        opc = True
    else:
        opc = False
    return opc


def generar_pass(length, caps, numbers, simbols):

    caracters = string.ascii_lowercase
    if caps:
        caracters += string.ascii_uppercase
    if numbers:
        caracters += string.digits
    if simbols:
        caracters += string.punctuation

    pass_final = ''.join(random.choice(caracters) for _ in range(length))
    return pass_final


print("Por defecto se colocaran minusculas")

9
length = int(input(
    "Ingrese el numero de caracteres que quiera poner (8 - 16), si coloca menos se pondran 8 por defecto: "))

if length < 8:
    length = 8


opc1 = input("Desea usar mayusculas? Y/N: ")
opc1 = true_false(opc1)

opc2 = input("Desea usar numeros? Y/N: ")
opc2 = true_false(opc2)

opc3 = input("Desea usar simbolos? Y/N: ")
opc3 = true_false(opc3)


print(generar_pass(length, opc1, opc2, opc3))

