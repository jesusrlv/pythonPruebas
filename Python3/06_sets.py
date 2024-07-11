### sets ###

# tiene arrays y listas, es una estructura fija que no se puede modificar

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialmente es un dict o diccionario

my_other_set = {"rodolfo","jesusrlv",43}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("JESUSRLV")

print(my_other_set) #no lo imprime ordenado

my_other_set.add("JESUSRLV")

print(my_other_set) #no adminte repetidos

print("rodolfo" in my_other_set)
print("jesus" in my_other_set)

my_other_set.remove("JESUSRLV")
print(my_other_set)

my_other_set.clear() #borra todos los elementos en el set
print(my_other_set)

my_set = {"rodolfo","jesusrlv",43}
my_list = list(my_set)
print((my_list))
print(my_list[0])

my_other_set = {"SQL","JS","PHP"}

my_new_set = my_set.union(my_other_set)

print(my_new_set)