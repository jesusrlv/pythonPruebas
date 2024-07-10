### tuplas ###

print("----------------------")
print("tuplas")
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (43, 1.95, "jesus", "jesusrlv")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("jesus")) #cuenta los elementos dentro de la tupla 
print(my_tuple.index("jesus")) #muestra el index de la tupla
print(my_tuple.index("jesusrlv")) #muestra el index de la tupla 