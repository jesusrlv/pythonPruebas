### Loops ###

#los while tiene else cosa que no tienen los demás lenguajes

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1 #sirve para autoincrementar
else: #el else es opcional
    print("Se terminó el while por la condición mayor o igual a 10")



while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("------------------------------------------------")
        print("mi condición es igual a 15")
        print("------------------------------------------------")
        break #rompe el bucle cuando la condición se cumple
    print(my_condition)

print("La ejecución continúa")

#los for son más eficientes que los while, ya que Python puede optimizarlos

print("------------------------------------------------")
print("lista")
print("------------------------------------------------")

my_list = [1,2,3,4,5,6,7]

for i in my_list:
    print(i)

print("------------------------------------------------")
print("tupla")
print("------------------------------------------------")

my_tuple = (43, 1.95, "jesus", "jesusrlv")

for i in my_tuple:
    print(i)

print("------------------------------------------------")
print("set")
print("------------------------------------------------")

my_set = {"rodolfo","jesusrlv",43}

for i in my_set:
    print(i)

print("------------------------------------------------")
print("diccionario sin valores")
print("------------------------------------------------")
my_dict = {"nombre": "jesusrlv","apellido":"leaños", "edad": 42}

for i in my_dict:
    print(i)

print("------------------------------------------------")
print("diccionario con valores")
print("------------------------------------------------")
my_dict = {"nombre": "jesusrlv","apellido":"leaños", "edad": 42}

for i in list(my_dict.values()):
    print(i)

print("------------------------------------------------")
print("else")
print("------------------------------------------------")
my_dict = {"nombre": "jesusrlv","apellido":"leaños", "edad": 42}

for i in list(my_dict.values()):
    print(i)
    if my_dict == "leaños":
        # print("encontró el 5")
        continue
    print("se ejecuta")
else:
    print("El bucle se terminó sin encontrar valores")