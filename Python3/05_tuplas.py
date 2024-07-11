### tuplas ###

print("----------------------")
print("tuplas")
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (43, 1.95, "jesus", "jesusrlv")
print(my_tuple)
print(type(my_tuple))

my_other_tuple = (30, 60, 30)

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("jesus")) #cuenta los elementos dentro de la tupla 
print(my_tuple.index("jesus")) #muestra el index de la tupla
print(my_tuple.index("jesusrlv")) #muestra el index de la tupla 

print("----------------------")
print("acceso a tuplas")

# my_tuple[1] = 1.99 no funciona porque ya está el valor constante definido
my_sum_tuple = my_tuple + my_other_tuple #suma tuplas
print(my_sum_tuple) #suma tuplas
print(my_sum_tuple[3:6]) #slice de tupla

my_list_tuple = list(my_sum_tuple)

print(type(my_sum_tuple))
print(type(my_list_tuple))

my_list_tuple[4] = "JESUSRLV"
my_list_tuple.insert(1, "Azul")

print(my_list_tuple)

my_list_tuple = (tuple(my_list_tuple))
print(my_list_tuple)
print(type(my_list_tuple))

print("----------------------")
print("borrar a tuplas")

del my_list_tuple