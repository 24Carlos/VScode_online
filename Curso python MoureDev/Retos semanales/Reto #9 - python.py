"""
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 """
"""
"""


"""
    heterograma, contiene las letras del alfabeto sin repetir, pueden repetirse si es mayuscuals 
    isograma, contiene una sola vez las letras sin repetir, no contiene espacios ni signos, solo letras
    pangrama, contiene al menos una vez una letra del abecedario
"""


def hetero(texto):
    for letras in texto:
        if texto.count(letras) > 1:
            # La función .count() se usa para contar el número de ocurrencias de las letras en la lista
            # Si esta es mayor a uno se retorna false
            return False
    return True


def isog(texto):
    texto = texto.lower()
    for letras in texto:
        if texto.count(letras) > 1:
            # La función .count() se usa para contar el número de ocurrencias de las letras en la lista
            # Si esta es mayor a uno se retorna false
            return False
    return True


texto_a_comprobar = input(
    "Ingrese un texto para comprobar si es un Heterograma: ")
print("------------")
if hetero(texto_a_comprobar):
    # Si la función hetero devuelve un true es que no se repite ninguna letra
    print(f"El texto [{texto_a_comprobar}] es un Heterograma")
else:
    # SI la funcion hetero devuelve false, es que se repitio una letra
    print(f"El texto [{texto_a_comprobar}] no es un Heterograma")
print("------------")


texto_a_comprobar = input(
    "Ingrese un texto para comprobar si es un Isograma: ")
print("------------")
if isog(texto_a_comprobar):
    print(f"El texto [{texto_a_comprobar}] es un Isograma")
else:
    print(f"El texto [{texto_a_comprobar}] no es un Isograma")
print("------------")
