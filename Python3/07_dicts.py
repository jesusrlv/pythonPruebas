### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"nombre": "jesusrlv","apellido":"leaños", "edad": 42}

my_dict ={
    "nombre": "rodolfo",
    "apellido": "leaños",
    "edad": 43, 
    "lenguajes": {"Python", "Swfit", "Dart"},
    1: 1.95
} 
print(my_dict)
print(my_other_dict)

print(len(my_dict))

my_dict["calle"] = "del pinar 111"

print(my_dict)

print("--------------------------------")
print("Eliminar")

del my_dict["calle"]
print(my_dict)

print("--------------------------------")
print("Buscar")

print("jesusrlv" in my_dict)
print("apellido" in my_dict)

print("--------------------------------")
print("news items")

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["nombre",1,"piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,("jesusrlv2","jesusRLV"))

print(my_new_dict)

