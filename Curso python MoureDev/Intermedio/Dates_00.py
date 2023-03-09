### Dates ###
from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime


def sep():
    print("------------------------------")


now = datetime.now()


print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp()


print(timestamp)


# Para crear una fecha y por ejemplo para el nueveo año

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


year_2023 = datetime(2023, 1, 1)
# lo minimo es el año, mes y dia, lo demas si no se pones es 0 por defecto
year_2023 = datetime(2023, 1, 1, 3)
print(year_2023)


print_date(now)
print_date(year_2023)

sep()
# from datetime import time


current_time = time(21, 6, 10)

print(current_time.hour)
print(current_time.minute)
print(current_time.min)
print(current_time.second)
# aca time no tiene datos y nosostros tenemos que ponerles


sep()
# from datetime import date

current_date = date(2023, 2, 24)
print(current_date)  # esto imprime 2024-02-23

print(current_date.year)
print(current_date.month)
print(current_date.day)

# Ya incicializado el current date ya sea en el año o en alguno de sus otros datos, se puede sumar

print(current_date.year)
print(current_date.year + 1)

# print(year_2023.date - current_date) No funciona para obtener la diferencia
#  entre 2 fechas


# Este si sirve entre los datos que tiene year 2023 y el now se hace la diferencia
diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)
sep()
# para crear un timedelta

init_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(f"{end_timedelta - init_timedelta} resta")
print(f"{end_timedelta + init_timedelta}  suma")
print(f"{end_timedelta / init_timedelta}  dividir")

