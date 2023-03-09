#El generador de pseudoaleatorio


 # Crea un generador de números pseudoaleatorios entre 0 y 100.
 # - No puedes usar ninguna función "random" (o semejante) del 
 #   lenguaje de programación seleccionado.

 # Es más complicado de lo que parece...


class GeneradorAleatorio:
    def __init__(self, numero1):
        self.numero1 = numero1

    def generar(self):
        a = 161
        c = 101
        m = 2*32
        self.numero1 = (a*self.numero1 + c) % m
        return self.numero1

generador = GeneradorAleatorio(2)
for i in range(5):
    print(generador.generar())



