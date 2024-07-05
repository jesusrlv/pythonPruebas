### Strings ###

my_string = "Mi cadena de texto"
my_other_string = 'Mi string'

print (len(my_string))
print (len(my_other_string))

print(my_string + my_other_string) #concatena

my_new_line = "Este es un String \n con salto de línea" #salto de línea
print(my_new_line)

my_tab_line = "\tEste es un String con tabulación" #tabulación de línea
print(my_tab_line)

my_escape_line = "\\Este es un String \\n escapado" #tabulación de línea
print(my_escape_line)


#formatear strings

name, surname, age = "jesus", "RLV", 9
print("Mi nombre es {} {} y mi edad es {}".format(name, surname,age)) #con format
print("Mi nombre es %s %s y mi edad es %s" %(name, surname,age)) #con %
print("Mi nombre es "+ name +" "+ surname +" y mi edad es " + str(age) ) #forma no recomendada
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #con inferencia de format por la f

#desempaquetado de caracteres
language = "Python" #guarda cada letra de la cadena te texto en cada variable
a , b , c , d, e , f= language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#división

language_slice = language[1:3] #corta desde la letra 1 y 3 (yt)
print(language_slice)
language_slice = language[1:] #corta desde la letra 1 hasta el final (ython)
print(language_slice)
language_slice = language[-2] #(o)
print(language_slice)
language_slice = language[0:6:2] #(o)
print(language_slice)

#reverse

reversed_language = language [::-1] #hace la cadena al revés
print(reversed_language)

#métodos o funciones del sistema

print(language.capitalize()) #pone la primer letra en mayúscula
print(language.upper()) #mayúsculas
print(language.count("t")) #contar
print(language.isnumeric()) #es numérico
print(language.lower()) #minúsculas
print(language.lower().isupper()) #minúsculas
print(language.startswith("Py")) #startswith si empieza con esa cadena
print("Py" == "py")

