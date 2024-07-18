## error types ##

# syntax error
#print "hola comunidad!"
print ("hola comunidad!")

# name error
language = "español" #se comentará para ver el error
print(language)

# IndexError
my_list = ["python", "swift", "kotlyn", "dart", "js"]
# print(my_list[-7]) este será el error al descomentar
print(my_list[-1])

#moduleNotFound
# import maths descomentar para ver error
import math

#attribute

# print(math.PI) el error
print(math.pi)

#key error

my_dict = {"nombre":"rodolfo","apellido":"leaños","edad":"42",1:"ptython"}
print(my_dict["edad"])
# print(my_dict["eda"])

#import error

# from math import pii #el error
from math import pi

#value error
my_int = "10"
# my_int = "10 años" #el error
print(int(my_int))

#ZeroDivision
print(0/4)
# print(4/0) #el error