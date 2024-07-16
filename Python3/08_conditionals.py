### Conditionals ###

my_condition = False

#esta condición se ejecuta si solo si es True
if my_condition :
    print("Se ejecutó condición del if")
my_condition = 5 * 5

if my_condition == 10:
    print("se ejecuta la segunda condición del if")

elif my_condition > 10 and my_condition < 20:
    print("es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("es igual a 1")

else:
    print("es menor o igual que 10 o mayor o igual que 20")


print("la ejecución continúa")

print("----------------------")
print("if con cadenas de texto")

my_string = ""
if not my_string:
    print("mi cadena de texto está null")
if my_string == "mi cadena de textoooo":
    print("mi otra cadena de texto no está vacía")