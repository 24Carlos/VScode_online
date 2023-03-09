class persona:
    def __init__(self, nombre, apellido, edad, ciudad):
        self.__name = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__ciudad = ciudad
        self.__informacion = f"El nombre de la persona es: {self.__name} con la edad de: {self.__edad}, y nació en {self.__ciudad}"

    def name_of_person(self):

        return self.__name

    def lastname_of_person(self):

        return self.__apellido

    def age_of_person(self):
        return self.__edad

    def city_of_person(self):
        return self.__ciudad

    def full_information(self):
        return self.__informacion


print("-------------------------")
manolous = persona("Manuel", "Perez", 22, "CDMX")


print(manolous.full_information())

"""Inveritr una cadena de texto"""


cadena = input("Ingrese el texto a inverir porfavor: ")
cadena_invertida = ""
for i in range(len(cadena)-1, -1, -1):
    cadena_invertida += cadena[i]
print("La cadena invertida es:", cadena_invertida)
