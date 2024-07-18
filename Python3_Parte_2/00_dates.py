## dates ##

from datetime import datetime as DateToday
now = DateToday.now()
print (now.day)
print (now.hour)
print (now.minute)
print (now.year)
print (now.month)
print (now.second)

def print_date(date):
    print (date.day)
    print (date.hour)
    print (date.minute)
    print (date.year)
    print (date.month)
    print (date.second)
    print (date.timestamp())

print_date(now)

timestamp = now.timestamp()

print(timestamp) #representa el tiempo, timestamp es una referencia desde 1970

new_year = DateToday(2024,1,1)

from datetime import time

current_time = time(21,6,0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date
current_date = date.today() #la fecha de hoy

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2024,10,6) #la fecha asignada manualmente

print(current_date.year)
print(current_date.month)
print(current_date.day)

fecha_annio = date(current_date.year, current_date.month + 1, current_date.day) 

print(current_date.month)

print("----------------------------")
print("fechas delta")

diff = new_year.date() - current_date
print(diff)

diff = new_year - now
print(diff)

from datetime import timedelta
#es para diferenciar dos fechas
start_timedelta = timedelta(200,100,100,weeks = 10)
end_timedelta = timedelta(300,100,100,weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
