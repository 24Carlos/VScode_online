### Funciones ### 

#⚠️ resolvemos 2 problemas, intentamos encapsular una logica muy concreto
#⚠️ evitamos errores y el codigo que resuelve estara en un unico lugar 

#⚠️ palabra para funciones es def

#def nombre_de_la_funcion():
    #contenido 



def my_funcion():
    print("Esto es un función") 

#⚠️ Una funcion puede recibir y hasta devolver codigo



my_funcion()
#my_funcion()
#my_funcion()

def sum_2_values(num1, num2):   #def() -> none
    if type(num1) != str and type(num2) != str :
        print(num1 + num2)
    elif type(num1) == bool and type(num2) == bool :
        print("")
    else:
        print("Por favor ingresar solo numeros 🤨")

print("-----------")
sum_2_values(4, 3)
sum_2_values(5213, 123894)
sum_2_values(4.2, 3.1)
sum_2_values("4", "3")

#🔷 Funciones que reciben pueden dar 

def sum_2_values_with_return(val1, val2):#    def() -> value
    return val1 + val2


my_result = sum_2_values_with_return(10, 2)
print(sum_2_values_with_return(10, 2))

print(my_result)

def print_name(name, surname):
    print(name + " " + surname)
    print(f"{name} {surname}") #⚠️ la f se usa para darle un formateo 

print_name(surname = "molina", name = "carlos") #se reordena como se introducen en el def 


    #Si alguien no mete el alias y que alias tenga un valor, así no peta el def xd
def print_name_whit_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}") #⚠️ la f se usa para darle un formateo 


print_name_whit_default("Carlos", "Molina", "fkrloss")
print_name_whit_default("Carlos", "Molina")



def print_texts(*text): #🔷 lo que hace es que este tipo de dato se le puede pasar la cantidad que sea
    print(text)


print_texts("asdasd", "Python", "MoureDev")
print_texts("asdasd")




#🔗 https://www.w3schools.com/python/python_functions.asp