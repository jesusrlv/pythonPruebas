## file handling ##
import os
# .txt file
txt_file = open("Python3_Parte_2/myFile.txt","w+")
txt_file.write("mi nombre es Rodolfo\nmi apellido es Leaños\n42 años\nmi nuevo lenguaje preferido es Python\ny también me gusta JS de a madres")
# txt_file.read()

# print(txt_file.read())
#print(txt_file.read(10)) #lee los 10 primeros caracteres
#print(txt_file.readline()) #lee por línea
#print(txt_file.readline()) #lee por línea
#print(txt_file.readlines()) #lee por línea con separaciones

for line in txt_file.readlines():
    print(line)

txt_file.write("\ny también me gusta JS de a madres")
print(txt_file.readline())

txt_file.close()

#os.remove("Python3_Parte_2/myFile.txt") #elimina el file

# .json file

import json

json_file = open("Python3_Parte_2/myFile.json", "w+")

json_test = {
    "nombre": "jesus",
    "surname": "rlv",
    "age": 42,
    "language": ["python", "swift", "php", "js"],
    "website": "http://dev.net"
    }
json.dump(json_test, json_file, indent = 8) #agrega el mapa de datos, luego pide el documento y al final la identanción que se da por espacios cada número
json_file.close() # se tiene que cerrar para poderlo leer en la consola
with open("Python3_Parte_2/myFile.json") as my_other_file: #se genera este para lerlo
    for line in my_other_file.readlines():
        print(line)