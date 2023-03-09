### Condicionales ###
#Domingo 8 de Enero

#⚠️ Un condicional es que si se cumple se ejecute algo o no 
def sep():
    print("---------")
sep()
sep()
sep()
my_condition = True
if my_condition: #⚠️ Es lo mismo que if my_condition == True:
    print("Se ejecuta la condicion del if ")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condicion del 2do if")

if my_condition > 10 and my_condition < 20: #⚠️ aca debe complir 2 condiciones en una 
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor que 20")
print(my_condition)
sep()



print("la Ejecución continua")

my_string = ""

if not my_string:
    print("Mi cadena de texto esta vacia")

if my_string == "mi cadena de textoooooo":
    print("Estas cadenas te texto coinciden")

#⚠️ Referencias 
#🔗 https://www.w3schools.com/python/python_conditions.asp 🔗