### listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35,24,62,52,30,30,17]

print(my_list)
print(len(my_list)) #el tamaño de cuántos datos tiene la lista

my_other_list = [35,1.90,"jesusrlv", "RLV"]


print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
#print(my_other_list[4]) error de rango
#print(my_other_list[-5]) error de rango

age, height, name, surnamen = my_other_list

print (name)
age, height, name, surnamen = my_other_list[2],my_other_list[1],my_other_list[0],my_other_list[3]

print(age)

print(my_list + my_other_list)

print([1,2,3,4])
#print(my_list - my_other_list)

my_list = "hola Python"
print(my_list)
print(type(my_list))