### Clases ### 



class MyEmptyPerson():
    pass #Esto es para evitar errores y "pasa" de esto

#print(MyEmptyPerson)
#print(MyEmptyPerson())



class Person():
    def __init__(self, name, surname, alias = "Sin alias"):
    #⚠️ para hacer una variable privada se hace con __ entre el self y la variable y se necesitara una función para solo leer la variable

        self.fullname = f"{name} {surname} [{alias}]" #⚠️ PROPIEDAD PUBLICA ⚠️
        self.__name = name #⚠️ PROPIEDAD PRIVADA ⚠️

    def walk(self):
        print(f"{self.fullname} Está caminando")

    def get_name(self):
        return self.__name

my_person = Person("Brais", "Moure")
print(my_person.fullname)

print(my_person.get_name())

my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.fullname)
my_other_person.walk()


my_other_person.fullname = "Hector de león (el loco de los perros)"
print(my_other_person.fullname)



#🔗 https://www.w3schools.com/python/python_classes.asp