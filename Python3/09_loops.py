### Loops ###

#los while tiene else cosa que no tienen los demás lenguajes

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1 #sirve para autoincrementar
else: #el else es opcional
    print("Se terminó el while por la condición mayor o igual a 10")

print("La ejecución continúa")