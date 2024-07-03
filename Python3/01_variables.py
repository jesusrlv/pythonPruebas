#variables python

my_variable_string = 'La variable es string'
print(my_variable_string)

my_var_int = 5
print(my_var_int)

my_int_to_str = str(my_var_int)
print(my_int_to_str)
print(type(my_int_to_str))

my_bool_var = True
print(my_bool_var)

#Concatenación de variables en un print
print(my_variable_string, my_int_to_str, my_bool_var)
print(type(print(my_variable_string,my_var_int,my_int_to_str,my_bool_var)))

print("Este es el valor de:",my_bool_var)

#función del sistema

print(len(my_variable_string))

#variables en una sola línea

name, surname, alias, age = "Rodolfo", "Leaños", "Rojo", 35
print("me llamo", name, "mi apellido es",surname,"mi age es:", age,"y mi alias es", alias)

#inputs de terminal

# first_name = input("Cuál es tu nombre: ")
# age = input("Cuál es tu edad: ")

print(name)
print(age)

#cambiar tipo
name = 35
age = "Brais"

print(name)
print(age)

#forzando el tipo, la primer línea se forza a que sea str
address: str = "Camino del pinar 111"
address = 32
print(type(address))

