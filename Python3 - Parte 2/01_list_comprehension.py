## list comprehension ##

my_original_list = [0,1,2,3,4,5,6,7]

my_range = range(8)
print(list(my_range))

my_list = [i for i in range(7)]
print(my_list)

my_list2 = [i + 1 for i in range(8)]
print(my_list2)

my_list2 = [i * 2 for i in range(8)]
print(my_list2)

my_list2 = [i * i for i in range(8)]
print(my_list2)

def sum_five(number):
    return number + 5

my_list2 = [sum_five(i) for i in range(8)]
print(my_list2)