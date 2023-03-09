"""
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del 
 *   lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
"""


def generar_numero_aleatorio(seed):
    a = 1103515245
    c = 12345
    m = 2**31
    numero = (a*seed + c) % m
    return numero % 101


# Generar 10 números pseudoaleatorios
semilla = 42
for i in range(10):
    numero_aleatorio = generar_numero_aleatorio(semilla)
    print(numero_aleatorio)
    semilla = numero_aleatorio
